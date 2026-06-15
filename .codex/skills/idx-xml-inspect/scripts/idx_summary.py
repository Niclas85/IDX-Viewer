#!/usr/bin/env python3
"""Summarize an IDX XML file without requiring schema files."""

from __future__ import annotations

import argparse
import collections
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def local_name(tag: str) -> str:
    if tag.startswith("{"):
        return tag.rsplit("}", 1)[1]
    return tag


def namespace_uri(tag: str) -> str:
    if tag.startswith("{"):
        return tag[1:].split("}", 1)[0]
    return ""


def child_text(element: ET.Element, child_local_name: str) -> str | None:
    for child in element:
        if local_name(child.tag) == child_local_name:
            return (child.text or "").strip()
    return None


def iter_by_local(root: ET.Element, name: str):
    for element in root.iter():
        if local_name(element.tag) == name:
            yield element


def user_properties(root: ET.Element):
    for prop in iter_by_local(root, "UserProperty"):
        key = None
        value = None
        for child in prop.iter():
            lname = local_name(child.tag)
            if lname == "ObjectName":
                key = (child.text or "").strip()
            elif lname == "Value":
                value = (child.text or "").strip()
        if key:
            yield key, value or ""


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize an IDX XML file.")
    parser.add_argument("idx_file", type=Path)
    parser.add_argument("--samples", type=int, default=8, help="sample count per section")
    args = parser.parse_args()

    try:
        tree = ET.parse(args.idx_file)
    except ET.ParseError as exc:
        print(f"XML parse error: {exc}", file=sys.stderr)
        return 2

    root = tree.getroot()
    counts = collections.Counter(local_name(el.tag) for el in root.iter())
    namespaces = sorted({namespace_uri(el.tag) for el in root.iter() if namespace_uri(el.tag)})
    ids = [el.attrib["id"] for el in root.iter() if "id" in el.attrib]
    duplicate_ids = [item for item, count in collections.Counter(ids).items() if count > 1]

    print(f"File: {args.idx_file}")
    print(f"Root: {local_name(root.tag)}")
    print(f"Namespaces: {len(namespaces)}")
    for uri in namespaces:
        print(f"  - {uri}")

    print("\nHeader")
    header = next(iter_by_local(root, "Header"), None)
    if header is None:
        print("  Header: missing")
    else:
        for key in ("CreatorName", "CreatorCompany", "CreatorSystem", "PostProcessor", "PostProcessorVersion", "GlobalUnitLength"):
            print(f"  {key}: {child_text(header, key) or ''}")

    print("\nUser properties")
    for key, value in list(user_properties(root))[: args.samples]:
        print(f"  {key}: {value}")

    print("\nElement counts")
    for name, count in counts.most_common(40):
        print(f"  {name}: {count}")

    print("\nIDs")
    print(f"  total: {len(ids)}")
    print(f"  duplicates: {len(duplicate_ids)}")
    for duplicate in duplicate_ids[: args.samples]:
        print(f"  duplicate: {duplicate}")

    print("\nItems")
    for item in list(iter_by_local(root, "Item"))[: args.samples]:
        print(f"  id={item.attrib.get('id', '')} type={child_text(item, 'ItemType') or ''}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
