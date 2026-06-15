---
name: idx-xml-inspect
description: Inspect, summarize, validate, or debug IDX XML files used for ECAD/MCAD collaboration. Use when Codex needs to parse .idx files, identify namespaces, header metadata, IDX mode/version, units, systems, persons, items, item instances, history entries, user properties, IDs, references, schema package elements, or malformed XML in this creo_ecad-import project.
---

# IDX XML Inspect

## Workflow

1. Treat `.idx` as XML. Parse with an XML parser and namespace-aware queries; do not rely on ad hoc string matching except for quick searches.
2. Start with `scripts/idx_summary.py <file.idx>` for a structural overview.
3. Inspect header metadata first: creator, post processor, global unit length, `IDX_MODE`, `IDX_VERSION`, systems, and history entries.
4. Count and sample important element families before changing code: `Item`, `ItemVersion`, `ItemInstance`, `ItemShape`, geometry, transformations, properties, and history.
5. Verify ID/reference integrity when debugging missing objects. Collect all `id` values and check references such as item definitions, shapes, units, systems, persons, and history subjects.
6. Preserve namespaces, element order, IDs, and original XML formatting expectations when editing IDX files.

## Reference

Read [references/idx-xml-notes.md](references/idx-xml-notes.md) when working beyond a quick summary.

The project reference document is `C:\Users\i00202914\Desktop\PSI5_IDXv4.5_Recommendation_Developer.pdf`.
