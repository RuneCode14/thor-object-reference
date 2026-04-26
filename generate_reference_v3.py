#!/usr/bin/env python3
"""
thor-object-reference v3
Convert THOR's --describe-object-type all JSON output into readable documentation.

Changes from v2:
- Field names shown in UPPERCASE (as used in Sigma rules), with lowercase JSON name noted
- More complete Sigma rule templates with multiple fields and realistic detection logic
- Nested object fields shown with UPPERCASE dot-notation (e.g., IMAGE|PATH, UNIT|HASHES|SHA256)

Usage:
    python3 generate-reference.py /path/to/thor-object-types.json --output-dir ./docs
"""

import json
import sys
import os
import argparse
from pathlib import Path
from typing import Any, Optional, Dict, List, Tuple

# Load example values database if available
EXAMPLES_DB = {}
_EXAMPLES_DB_PATH = Path(__file__).parent / "examples_db.yml"
if _EXAMPLES_DB_PATH.exists():
    try:
        import yaml
        with open(_EXAMPLES_DB_PATH, "r") as f:
            EXAMPLES_DB = yaml.safe_load(f) or {}
    except Exception:
        pass


def get_ref_name(ref: str) -> str:
    """Extract definition name from a $ref string like '#/$defs/LinuxKernelModule'."""
    if ref.startswith("#/$defs/"):
        return ref[8:]
    if ref.startswith("#/definitions/"):
        return ref[14:]
    return ref.split("/")[-1]


def resolve_ref(ref: str, defs: dict) -> dict:
    """Resolve a $ref to its definition."""
    name = get_ref_name(ref)
    return defs.get(name, {})


def get_type_label(field_schema: dict, defs: dict) -> str:
    """Extract a human-readable type label for a field."""
    if not isinstance(field_schema, dict):
        return str(field_schema) if field_schema is not None else "null"

    if "$ref" in field_schema:
        ref_name = get_ref_name(field_schema["$ref"])
        return ref_name

    t = field_schema.get("type", "any")
    fmt = field_schema.get("format", "")
    items = field_schema.get("items", {})

    if t == "array":
        if isinstance(items, dict) and "$ref" in items:
            return f"array of {get_ref_name(items['$ref'])}"
        elif isinstance(items, dict) and "type" in items:
            return f"array of {items['type']}"
        return "array"

    if "anyOf" in field_schema:
        types = []
        for opt in field_schema["anyOf"]:
            if isinstance(opt, dict) and "$ref" in opt:
                types.append(get_ref_name(opt["$ref"]))
            elif isinstance(opt, dict):
                types.append(opt.get("type", "any"))
            else:
                types.append(str(opt))
        return " | ".join(sorted(set(types)))

    if "oneOf" in field_schema:
        types = []
        for opt in field_schema["oneOf"]:
            if isinstance(opt, dict) and "$ref" in opt:
                types.append(get_ref_name(opt["$ref"]))
            elif isinstance(opt, dict):
                types.append(opt.get("type", "any"))
            else:
                types.append(str(opt))
        return " | ".join(sorted(set(types)))

    if "additionalProperties" in field_schema:
        if isinstance(field_schema["additionalProperties"], dict):
            return f"object ({field_schema['additionalProperties'].get('type', 'any')})"
        return "object"

    label = t
    if fmt:
        label += f" ({fmt})"
    return label


def get_description(field_schema: dict) -> str:
    """Try to extract or infer a description."""
    if not isinstance(field_schema, dict):
        return ""
    return field_schema.get("description", "")


def resolve_properties(def_obj: dict, defs: dict) -> Dict[str, dict]:
    """
    Resolve all properties for a definition object, following $ref and allOf.
    Returns a flat dict of {field_name: resolved_schema}.
    """
    if not isinstance(def_obj, dict):
        return {}

    if "$ref" in def_obj:
        resolved = resolve_ref(def_obj["$ref"], defs)
        return resolve_properties(resolved, defs)

    props = {}
    required = set()

    if "properties" in def_obj and isinstance(def_obj["properties"], dict):
        props.update(def_obj["properties"])

    if "required" in def_obj:
        required.update(def_obj["required"])

    for sub in def_obj.get("allOf", []):
        sub_props = resolve_properties(sub, defs)
        if isinstance(sub, dict) and "properties" in sub:
            props.update(sub["properties"])
        if isinstance(sub, dict) and "required" in sub:
            required.update(sub["required"])
        elif sub_props:
            props.update(sub_props)

    for name in props:
        if not isinstance(props[name], dict):
            props[name] = {"_type": props[name]}
        if name in required:
            props[name]["_required"] = True

    return props


def flatten_references(field_schema: dict, defs: dict, depth: int = 0) -> dict:
    """
    Recursively flatten $ref references in a field schema for display purposes.
    Returns a simplified schema dict.
    """
    if depth > 5:
        return {"_max_depth": True}
    if not isinstance(field_schema, dict):
        return field_schema

    if "$ref" in field_schema:
        resolved = resolve_ref(field_schema["$ref"], defs)
        merged = flatten_references(resolved, defs, depth + 1)
        if isinstance(merged, dict):
            merged["_ref"] = get_ref_name(field_schema["$ref"])
        return merged

    result = {}
    for k, v in field_schema.items():
        k_lower = k.lower()
        if k_lower == "properties" and isinstance(v, dict):
            result[k] = {nk: flatten_references(nv, defs, depth + 1) for nk, nv in v.items()}
        elif k_lower == "items" and isinstance(v, dict):
            result[k] = flatten_references(v, defs, depth + 1)
        elif k_lower == "allof" and isinstance(v, list):
            result[k] = [flatten_references(item, defs, depth + 1) for item in v]
        elif k_lower == "anyof" and isinstance(v, list):
            result[k] = [flatten_references(item, defs, depth + 1) for item in v]
        elif k_lower == "oneof" and isinstance(v, list):
            result[k] = [flatten_references(item, defs, depth + 1) for item in v]
        elif k_lower == "additionalproperties" and isinstance(v, dict):
            result[k] = flatten_references(v, defs, depth + 1)
        else:
            result[k] = v
    return result


def get_nested_fields_flat(flat_schema: dict, defs: dict, sigma_prefix: str = "", json_prefix: str = "", depth: int = 0) -> List[Tuple[str, str, str]]:
    """
    Extract nested sub-fields as flat (sigma_name, type, json_name) tuples.
    sigma_name uses UPPERCASE with | separator (e.g., IMAGE|PATH).
    json_name uses lowercase with . separator (e.g., image.path).
    
    sigma_prefix/json_prefix track the accumulated path independently.
    """
    if depth > 3 or not isinstance(flat_schema, dict):
        return []

    nested = []

    if "properties" in flat_schema:
        for sub_name, sub_schema in flat_schema["properties"].items():
            if not isinstance(sub_schema, dict):
                continue
            sub_type = get_type_label(sub_schema, defs)
            sigma_name = f"{sigma_prefix}{sub_name.upper()}" if sigma_prefix else sub_name.upper()
            json_name = f"{json_prefix}{sub_name}" if json_prefix else sub_name

            # If it's a nested object with its own properties, recurse
            sub_flat = flatten_references(sub_schema, defs) if "$ref" in sub_schema else sub_schema
            if isinstance(sub_flat, dict) and "properties" in sub_flat:
                deeper = get_nested_fields_flat(
                    sub_flat, defs,
                    sigma_prefix=f"{sigma_name}|",
                    json_prefix=f"{json_name}.",
                    depth=depth + 1
                )
                nested.extend(deeper)
            else:
                nested.append((sigma_name, sub_type, json_name))
    elif flat_schema.get("type") == "array" and "items" in flat_schema:
        items = flat_schema["items"]
        if isinstance(items, dict) and "$ref" in items:
            items_flat = flatten_references(items, defs)
            if isinstance(items_flat, dict) and "properties" in items_flat:
                deeper = get_nested_fields_flat(
                    items_flat, defs,
                    sigma_prefix=sigma_prefix,
                    json_prefix=json_prefix,
                    depth=depth + 1
                )
                nested.extend(deeper)

    return nested


def get_nested_fields(flat_schema: dict, defs: dict, parent_sigma: str = "", parent_json: str = "") -> List[Tuple[str, str]]:
    """Extract nested sub-fields for display (sigma_name, type)."""
    results = get_nested_fields_flat(flat_schema, defs, sigma_prefix=parent_sigma, json_prefix=parent_json)
    return [(s, t) for s, t, j in results]


def sigma_field_name(json_name: str) -> str:
    """Convert a lowercase JSON field name to UPPERCASE Sigma field name."""
    return json_name.upper()


def guess_field_category(field_name: str, field_schema: dict) -> str:
    """Guess a semantic category for a field to help build better Sigma templates."""
    name_lower = field_name.lower()
    ftype = ""
    if isinstance(field_schema, dict):
        if "$ref" in field_schema:
            ftype = get_ref_name(field_schema["$ref"]).lower()
        else:
            ftype = str(field_schema.get("type", ""))

    if "path" in name_lower and ftype in ("string", ""):
        return "path"
    if "command" in name_lower and "string" in ftype:
        return "command"
    if "hash" in name_lower or name_lower == "hashes":
        return "hash"
    if "ip" in name_lower and "string" in ftype:
        return "ip"
    if "port" in name_lower and ftype in ("string", "integer"):
        return "port"
    if "user" in name_lower and "string" in ftype:
        return "user"
    if "name" in name_lower and "string" in ftype:
        return "name"
    if "image" in name_lower and ftype in ("file", "object", ""):
        return "image"
    if "file" in name_lower and ftype in ("file", "object", ""):
        return "file"
    if "service" in name_lower and "string" in ftype:
        return "service"
    if "description" in name_lower and "string" in ftype:
        return "description"
    if name_lower == "type" and ftype == "string":
        return "type"
    if name_lower == "exists" and ftype == "string":
        return "exists"
    if name_lower == "signed" and ftype == "boolean":
        return "signed"
    if name_lower == "size" and ftype == "integer":
        return "size"
    return "generic"


def generate_sigma_template(type_name: str, flattened_props: dict, required: set, defs: dict) -> str:
    """Generate a realistic, complex Sigma rule template based on the object type's fields."""
    lines = []
    lines.append("logsource:")
    lines.append("    product: THOR")
    lines.append(f'    service: "{type_name}"')
    lines.append("")

    # Categorize fields for template building
    path_fields = []       # file/path - use |contains
    command_fields = []    # command strings - use |contains|endswith
    name_fields = []       # name strings - use |contains
    user_fields = []       # user/group - use filter
    hash_fields = []       # hashes - use exact match
    bool_fields = []       # boolean flags
    image_fields = []       # file objects (IMAGE, FILE, UNIT)
    ip_fields = []          # IP addresses
    port_fields = []        # port numbers
    type_fields = []        # type category
    other_string_fields = []

    for field_name in sorted(flattened_props.keys()):
        field_schema = flattened_props[field_name]
        cat = guess_field_category(field_name, field_schema)
        if cat == "path":
            path_fields.append(field_name)
        elif cat == "command":
            command_fields.append(field_name)
        elif cat == "name":
            name_fields.append(field_name)
        elif cat == "user":
            user_fields.append(field_name)
        elif cat == "hash":
            hash_fields.append(field_name)
        elif cat == "signed":
            bool_fields.append(field_name)
        elif cat == "exists":
            bool_fields.append(field_name)
        elif cat == "image" or cat == "file":
            image_fields.append(field_name)
        elif cat == "ip":
            ip_fields.append(field_name)
        elif cat == "port":
            port_fields.append(field_name)
        elif cat == "type":
            type_fields.append(field_name)
        elif cat == "service":
            name_fields.append(field_name)
        elif cat == "size":
            pass  # skip size in templates
        else:
            other_string_fields.append(field_name)

    # Build selection block
    selection_parts = []
    filter_parts = []

    # Image/file path detection
    if image_fields:
        for fname in image_fields[:2]:  # Use top 2 image fields
            sigma_parent = sigma_field_name(fname)
            nested = get_nested_fields_flat(flattened_props[fname], defs)
            # Find PATH sub-field
            path_sub = next(((s, t, j) for s, t, j in nested if s.endswith("|PATH") or s == "PATH"), None)
            if path_sub:
                selection_parts.append((path_sub[0] + "|contains", [
                    "'/tmp/'",
                    "'/dev/shm/'",
                    "'\\\\Temp\\\\'"
                ]))
            # Find SIGNATURE/SIGNED sub-field for filter
            signed_sub = next(((s, t, j) for s, t, j in nested if "SIGNED" in s), None)
            if signed_sub and signed_sub[1] == "boolean":
                filter_parts.append((signed_sub[0], "'true'"))

    # Path-based fields (non-image)
    for fname in path_fields[:1]:
        sigma = sigma_field_name(fname)
        selection_parts.append((f"{sigma}|contains", [
            "'/suspicious/'",
            "'/tmp/'"
        ]))

    # Command fields
    for fname in command_fields[:1]:
        sigma = sigma_field_name(fname)
        selection_parts.append((f"{sigma}|contains|all", [
            "'powershell'",
            "'-encodedcommand'"
        ]))

    # Name fields
    for fname in name_fields[:1]:
        sigma = sigma_field_name(fname)
        selection_parts.append((f"{sigma}|contains", [
            "'suspicious'",
            "'malware'"
        ]))

    # User fields - for filtering legitimate users
    for fname in user_fields[:1]:
        sigma = sigma_field_name(fname)
        filter_parts.append((f"{sigma}|contains", [
            "'root'",
            "'system'"
        ]))

    # Hash fields
    for fname in hash_fields[:1]:
        sigma = sigma_field_name(fname)
        nested = get_nested_fields_flat(flattened_props[fname], defs)
        sha256 = next(((s, t, j) for s, t, j in nested if "SHA256" in s), None)
        if sha256:
            selection_parts.append((sha256[0], "'known_bad_hash_sha256'"))

    # Boolean fields for filter
    for fname in bool_fields[:2]:
        sigma = sigma_field_name(fname)
        filter_parts.append((sigma, "'true'"))

    # Type fields
    for fname in type_fields[:1]:
        sigma = sigma_field_name(fname)
        selection_parts.append((sigma, "'relevant_type'"))

    # IP fields
    for fname in ip_fields[:1]:
        sigma = sigma_field_name(fname)
        selection_parts.append((f"{sigma}|contains", [
            "'192.168.'",
            "'10.'"
        ]))

    # Fallback: use first required string field if nothing matched
    if not selection_parts and flattened_props:
        for fname in sorted(flattened_props.keys()):
            if fname in required:
                sigma = sigma_field_name(fname)
                selection_parts.append((f"{sigma}|contains", ["'suspicious'"]))
                break
        if not selection_parts:
            first = sorted(flattened_props.keys())[0]
            selection_parts.append((f"{sigma_field_name(first)}|contains", ["'suspicious'"]))

    # Build the YAML output
    lines.append("detection:")
    lines.append("    selection:")

    if len(selection_parts) == 1:
        key, values = selection_parts[0]
        if isinstance(values, list):
            if len(values) == 1:
                lines.append(f"        {key}: {values[0]}")
            else:
                lines.append(f"        {key}:")
                for v in values:
                    lines.append(f"            - {v}")
        else:
            lines.append(f"        {key}: {values}")
    else:
        for key, values in selection_parts:
            if isinstance(values, list):
                if len(values) == 1:
                    lines.append(f"        {key}: {values[0]}")
                else:
                    lines.append(f"        {key}:")
                    for v in values:
                        lines.append(f"            - {v}")
            else:
                lines.append(f"        {key}: {values}")

    if filter_parts:
        lines.append("    filter_legitimate:")
        for key, values in filter_parts:
            if isinstance(values, list):
                lines.append(f"        {key}:")
                for v in values:
                    lines.append(f"            - {v}")
            else:
                lines.append(f"        {key}: {values}")

    if filter_parts:
        lines.append("    condition: selection and not filter_legitimate")
    else:
        lines.append("    condition: selection")

    return "\n".join(lines)


def generate_markdown(type_name: str, schema: dict) -> str:
    """Generate a Markdown document for a single object type."""
    defs = schema.get("$defs", {})

    ref = schema.get("$ref", "")
    root_def = resolve_ref(ref, defs)
    root_name = get_ref_name(ref) if ref else ""

    if not root_def and defs:
        for dn, dd in defs.items():
            if dn.lower() == type_name.replace(" ", "").lower():
                root_def = dd
                root_name = dn
                break
        if not root_def:
            root_def = next(iter(defs.values()))
            root_name = next(iter(defs.keys()))

    all_props = resolve_properties(root_def, defs)

    flattened_props = {}
    for name, prop_schema in all_props.items():
        flattened_props[name] = flatten_references(prop_schema, defs)

    required = set()
    if "required" in root_def:
        required = set(root_def["required"])
    for sub in root_def.get("allOf", []):
        if isinstance(sub, dict) and "required" in sub:
            required.update(sub["required"])

    doc = []
    doc.append(f"# {type_name}")
    doc.append("")

    # Metadata
    meta = []
    if "$id" in schema:
        meta.append(f"**Schema ID:** `{schema['$id']}`")
    if "$schema" in schema:
        meta.append(f"**JSON Schema:** `{schema['$schema']}`")
    if root_name:
        meta.append(f"**Definition:** `{root_name}`")
    if meta:
        doc.append(" | ".join(meta))
        doc.append("")

    desc = root_def.get("description", "")
    if desc:
        doc.append(desc)
        doc.append("")

    if not flattened_props:
        doc.append("_No fields defined._")
        doc.append("")
        return "\n".join(doc)

    # Field reference table — UPPERCASE Sigma names with lowercase JSON names
    doc.append("## Fields")
    doc.append("")
    doc.append("Field names are shown in **UPPERCASE** as used in Sigma rules.")
    doc.append("The lowercase JSON name is shown in parentheses for reference.")
    doc.append("")
    doc.append("| Sigma Field | JSON Name | Type | Required | Description | Example Values |")
    doc.append("|-------------|-----------|------|----------|-------------|----------------|")

    for field_name in sorted(flattened_props.keys()):
        field_schema = flattened_props[field_name]
        ftype = get_type_label(field_schema, defs)
        req = "✅" if field_name in required else ""
        desc = get_description(field_schema)
        desc = desc.replace("|", "\\|")

        # Nested fields
        nested = get_nested_fields(field_schema, defs)
        if nested:
            nested_desc = "; ".join([f"`{n}`: {t}" for n, t in nested])
            if desc:
                desc += f" — nested: {nested_desc}"
            else:
                desc = f"nested: {nested_desc}"

        sigma_name = sigma_field_name(field_name)
        
        # Look up example values for this field
        examples = []
        type_key = type_name.lower()
        if type_key in EXAMPLES_DB:
            # Check exact field name match
            if field_name in EXAMPLES_DB[type_key]:
                examples = EXAMPLES_DB[type_key][field_name]
            # Also check sigma name match
            elif sigma_name in EXAMPLES_DB[type_key]:
                examples = EXAMPLES_DB[type_key][sigma_name]
        
        example_str = ""
        if examples:
            # Truncate long examples and join with commas
            display = [f"`{str(e)[:40]}{'...' if len(str(e)) > 40 else ''}`" for e in examples[:3]]
            example_str = ", ".join(display)
        
        doc.append(f"| `{sigma_name}` | `{field_name}` | {ftype} | {req} | {desc} | {example_str} |")

    # Nested field reference for complex types
    doc.append("")
    doc.append("### Nested Field Reference (Sigma Pipe Notation)")
    doc.append("")
    doc.append("Complex types like `File` have nested fields accessed with `|` in Sigma:")
    doc.append("")

    has_nested = False
    for field_name in sorted(flattened_props.keys()):
        field_schema = flattened_props[field_name]
        nested_flat = get_nested_fields_flat(field_schema, defs)
        if nested_flat:
            has_nested = True
            sigma_parent = sigma_field_name(field_name)
            doc.append(f"**{sigma_parent}** (`{field_name}` — {get_type_label(field_schema, defs)}):")
            doc.append("")
            doc.append("| Sigma Field | JSON Path | Type |")
            doc.append("|-------------|-----------|------|")
            for s, t, j in nested_flat:
                doc.append(f"| `{s}` | `{j}` | {t} |")
            doc.append("")

    if not has_nested:
        doc.append("_No nested fields in this type._")
        doc.append("")

    # Sigma rule template
    doc.append("## Sigma Rule Template")
    doc.append("")
    doc.append("```yaml")
    sigma_tmpl = generate_sigma_template(type_name, flattened_props, required, defs)
    doc.append(sigma_tmpl)
    doc.append("```")
    doc.append("")

    return "\n".join(doc)


def generate_yaml(type_name: str, schema: dict) -> str:
    """Generate a YAML document for a single object type."""
    try:
        import yaml
    except ImportError:
        return "# PyYAML not installed\n"

    defs = schema.get("$defs", {})
    ref = schema.get("$ref", "")
    root_def = resolve_ref(ref, defs)
    if not root_def and defs:
        for dn, dd in defs.items():
            if dn.lower() == type_name.replace(" ", "").lower():
                root_def = dd
                break
        if not root_def:
            root_def = next(iter(defs.values()))

    all_props = resolve_properties(root_def, defs)
    required = set()
    if "required" in root_def:
        required = set(root_def["required"])
    for sub in root_def.get("allOf", []):
        if isinstance(sub, dict) and "required" in sub:
            required.update(sub["required"])

    flattened_props = {}
    for name, prop_schema in all_props.items():
        flattened_props[name] = flatten_references(prop_schema, defs)

    obj = {
        "name": type_name,
        "schema": schema.get("$id", ""),
        "fields": []
    }
    for field_name in sorted(all_props.keys()):
        field_schema = all_props[field_name]
        flat = flatten_references(field_schema, defs)
        nested = get_nested_fields_flat(flat, defs)
        field_entry = {
            "sigma_name": sigma_field_name(field_name),
            "json_name": field_name,
            "type": get_type_label(flat, defs),
            "required": field_name in required,
            "description": get_description(flat)
        }
        if nested:
            field_entry["nested"] = [
                {"sigma_name": s, "json_name": j, "type": t}
                for s, t, j in nested
            ]
        obj["fields"].append(field_entry)

    return yaml.dump(obj, sort_keys=False, allow_unicode=True)


def generate_summary(json_data: dict, output_dir: Path) -> str:
    """Generate the main README / summary index."""
    doc = []
    doc.append("# THOR Object Type Reference")
    doc.append("")
    doc.append(f"Source: THOR `--describe-object-type all` ({len(json_data)} object types)")
    doc.append("")
    doc.append("This reference maps every THOR object type to its available fields, types, and required status.")
    doc.append("Use it when writing custom Sigma rules with `product: THOR`.")
    doc.append("")
    doc.append("**Field naming convention:**")
    doc.append("- In THOR JSON output: **lowercase** with underscores (e.g., `run_as_user`)")
    doc.append("- In Sigma rules: **UPPERCASE** (e.g., `RUN_AS_USER`)")
    doc.append("- Nested fields use **pipe notation** in Sigma (e.g., `IMAGE|PATH`, `UNIT|HASHES|SHA256`)")
    doc.append("")

    # Category grouping
    categories = {}
    for type_name in sorted(json_data.keys()):
        defs = json_data[type_name].get("$defs", {})
        ref = json_data[type_name].get("$ref", "")
        root_def = resolve_ref(ref, defs)
        if not root_def and defs:
            for dn, dd in defs.items():
                if dn.lower() == type_name.replace(" ", "").lower():
                    root_def = dd
                    break
            if not root_def:
                root_def = next(iter(defs.values()))

        props = resolve_properties(root_def, defs)
        field_count = len(props)

        name_lower = type_name.lower()
        if any(x in name_lower for x in ["platform information"]):
            cat = "Platform"
        elif any(x in name_lower for x in ["process", "thread", "handle"]):
            cat = "Process & Memory"
        elif any(x in name_lower for x in ["service", "cron job", "scheduled task", "autorun", "kernel module", "at job", "wmi"]):
            cat = "Persistence & System"
        elif any(x in name_lower for x in ["file", "mft", "prefetch", "jump list", "shim"]):
            cat = "File System"
        elif any(x in name_lower for x in ["registry"]):
            cat = "Registry"
        elif any(x in name_lower for x in ["user", "lsa", "authorized_keys", "logged in"]):
            cat = "Identity & Auth"
        elif any(x in name_lower for x in ["dns", "network", "firewall", "hosts", "share", "connection", "session", "share"]):
            cat = "Network"
        elif any(x in name_lower for x in ["eventlog", "log ", "journal", "audit", "log"]):
            cat = "Logs & Events"
        elif any(x in name_lower for x in ["amcache", "web ", "download", "visit"]):
            cat = "Execution History"
        elif any(x in name_lower for x in ["mutex", "pipe", "antivirus"]):
            cat = "Security & Kernel"
        else:
            cat = "Other"

        categories.setdefault(cat, []).append((type_name, field_count))

    for cat in categories:
        doc.append(f"## {cat}")
        doc.append("")
        doc.append("| Object Type | Fields | Sigma Service |")
        doc.append("|-------------|--------|---------------|")
        for type_name, field_count in categories[cat]:
            md_file = type_name_to_filename(type_name) + ".md"
            doc.append(f"| [{type_name}](docs/{md_file}) | {field_count} | `product: THOR, service: \"{type_name}\"` |")
        doc.append("")

    return "\n".join(doc)


def type_name_to_filename(type_name: str) -> str:
    return type_name.lower().replace(" ", "-").replace("/", "-")


def main():
    parser = argparse.ArgumentParser(description="Convert THOR object types to reference docs (v3).")
    parser.add_argument("input", help="Path to THOR --describe-object-type all JSON")
    parser.add_argument("--output-dir", "-o", default="./docs", help="Output directory (default: ./docs)")
    parser.add_argument("--format", "-f", default="both", choices=["markdown", "yaml", "both"])
    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        data = json.load(f)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    types_list = sorted(data.keys())

    for type_name in types_list:
        base = type_name_to_filename(type_name)
        schema = data[type_name]

        if args.format in ("markdown", "both"):
            md_path = output_dir / f"{base}.md"
            md_path.write_text(generate_markdown(type_name, schema), encoding="utf-8")

        if args.format in ("yaml", "both"):
            yaml_path = output_dir / f"{base}.yml"
            yaml_path.write_text(generate_yaml(type_name, schema), encoding="utf-8")

    # Generate summary README
    readme = generate_summary(data, output_dir)
    (output_dir / "README.md").write_text(readme, encoding="utf-8")

    print(f"Generated {len(types_list)} object type references in {output_dir}")


if __name__ == "__main__":
    main()