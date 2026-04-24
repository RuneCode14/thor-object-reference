#!/usr/bin/env python3
"""
thor-object-reference
Convert THOR's --describe-object-type all JSON output into readable documentation.

Usage:
    python3 generate-reference.py /path/to/thor-object-types.json --output-dir ./docs
"""

import json
import sys
import os
import argparse
from pathlib import Path
from typing import Any, Optional, Dict


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
        # Avoid resolving the full ref recursively for the label
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

    # Resolve $ref first
    if "$ref" in def_obj:
        resolved = resolve_ref(def_obj["$ref"], defs)
        return resolve_properties(resolved, defs)

    props = {}
    required = set()

    # Direct properties
    if "properties" in def_obj and isinstance(def_obj["properties"], dict):
        props.update(def_obj["properties"])

    if "required" in def_obj:
        required.update(def_obj["required"])

    # allOf merge
    for sub in def_obj.get("allOf", []):
        sub_props = resolve_properties(sub, defs)
        if isinstance(sub, dict) and "properties" in sub:
            props.update(sub["properties"])
        if isinstance(sub, dict) and "required" in sub:
            required.update(sub["required"])
        elif sub_props:
            props.update(sub_props)

    # Mark required fields in the final props dict
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
        # Keep the original ref name
        if isinstance(merged, dict):
            merged["_ref"] = get_ref_name(field_schema["$ref"])
        return merged

    result = {}
    for k, v in field_schema.items():
        if k == "properties" and isinstance(v, dict):
            result[k] = {nk: flatten_references(nv, defs, depth + 1) for nk, nv in v.items()}
        elif k == "items" and isinstance(v, dict):
            result[k] = flatten_references(v, defs, depth + 1)
        elif k == "allOf" and isinstance(v, list):
            result[k] = [flatten_references(item, defs, depth + 1) for item in v]
        elif k == "anyOf" and isinstance(v, list):
            result[k] = [flatten_references(item, defs, depth + 1) for item in v]
        elif k == "oneOf" and isinstance(v, list):
            result[k] = [flatten_references(item, defs, depth + 1) for item in v]
        elif k == "additionalProperties" and isinstance(v, dict):
            result[k] = flatten_references(v, defs, depth + 1)
        else:
            result[k] = v
    return result


def get_nested_fields(flat_schema: dict, defs: dict) -> list:
    """Extract nested sub-fields for display, if any."""
    if not isinstance(flat_schema, dict):
        return []
    nested = []
    ref_name = flat_schema.get("_ref", "")
    if "properties" in flat_schema:
        for sub_name, sub_schema in flat_schema["properties"].items():
            sub_type = get_type_label(sub_schema, defs)
            nested.append((sub_name, sub_type))
    elif flat_schema.get("type") == "array" and "items" in flat_schema:
        items = flat_schema["items"]
        if isinstance(items, dict) and "properties" in items:
            for sub_name, sub_schema in items["properties"].items():
                sub_type = get_type_label(sub_schema, defs)
                nested.append((sub_name, sub_type))
    return nested


def generate_markdown(type_name: str, schema: dict) -> str:
    """Generate a Markdown document for a single object type."""
    defs = schema.get("$defs", {})

    # Find the root definition via $ref
    ref = schema.get("$ref", "")
    root_def = resolve_ref(ref, defs)
    root_name = get_ref_name(ref) if ref else ""

    if not root_def and defs:
        # Fallback: use the first definition that matches the type name
        for dn, dd in defs.items():
            if dn.lower() == type_name.replace(" ", "").lower():
                root_def = dd
                root_name = dn
                break
        if not root_def:
            root_def = next(iter(defs.values()))
            root_name = next(iter(defs.keys()))

    # Resolve and flatten properties
    all_props = resolve_properties(root_def, defs)

    # Flatten references in each property
    flattened_props = {}
    for name, prop_schema in all_props.items():
        flattened_props[name] = flatten_references(prop_schema, defs)

    # Collect required
    required = set()
    if "required" in root_def:
        required = set(root_def["required"])
    # Also check in allOf
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

    doc.append("## Fields")
    doc.append("")
    doc.append("| Field | Type | Required | Description |")
    doc.append("|-------|------|----------|-------------|")

    for field_name in sorted(flattened_props.keys()):
        field_schema = flattened_props[field_name]
        ftype = get_type_label(field_schema, defs)
        req = "✅" if field_name in required else ""
        desc = get_description(field_schema)
        desc = desc.replace("|", "\\|")

        # Add nested fields to description
        nested = get_nested_fields(field_schema, defs)
        if nested:
            nested_desc = "; ".join([f"`{n}`: {t}" for n, t in nested])
            if desc:
                desc += f" — nested: {nested_desc}"
            else:
                desc = f"nested: {nested_desc}"

        doc.append(f"| `{field_name}` | {ftype} | {req} | {desc} |")

    doc.append("")

    # Example Sigma rule
    doc.append("## Sigma Rule Template")
    doc.append("")
    doc.append("```yaml")
    doc.append("logsource:")
    doc.append("    product: THOR")
    doc.append(f'    service: "{type_name}"')
    doc.append("")
    doc.append("detection:")
    doc.append("    selection:")
    if flattened_props:
        first_field = sorted(flattened_props.keys())[0]
        doc.append(f"        {first_field.upper()}: null")
    doc.append("    condition: selection")
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

    obj = {
        "name": type_name,
        "schema": schema.get("$id", ""),
        "fields": []
    }
    for field_name in sorted(all_props.keys()):
        field_schema = all_props[field_name]
        flat = flatten_references(field_schema, defs)
        obj["fields"].append({
            "name": field_name,
            "type": get_type_label(flat, defs),
            "required": field_name in required,
            "description": get_description(flat)
        })

    return yaml.dump(obj, sort_keys=False, allow_unicode=True)


def generate_summary(json_data: dict, output_dir: Path) -> str:
    """Generate the main README / summary index."""
    doc = []
    doc.append("# THOR Object Type Reference")
    doc.append("")
    doc.append(f"Source: THOR `--describe-object-type all` ({len(json_data)} object types)")
    doc.append("")
    doc.append("This reference maps every THOR object type to its available fields, types, and required status.")
    doc.append("Use it when writing custom Sigma rules with `product: THOR`. Fields are **UPPERCASE** in Sigma.")
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
        elif any(x in name_lower for x in ["process", "thread", "handle"]):  # removed memory
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
    parser = argparse.ArgumentParser(description="Convert THOR object types to reference docs.")
    parser.add_argument("input", help="Path to THOR --describe-object-type all JSON")
    parser.add_argument("--output-dir", "-o", default="./docs", help="Output directory (default: ./docs)")
    parser.add_argument("--format", "-f", default="markdown", choices=["markdown", "yaml", "both"])
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
