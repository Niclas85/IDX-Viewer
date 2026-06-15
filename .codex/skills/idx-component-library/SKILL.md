---
name: idx-component-library
description: Model, inspect, or debug IDX standardized library component data, component bodies, pins, electrical insertion points, padstack names, component thermal properties, value/tolerance properties, materials, item definitions, component instances, and ECAD/MCAD library exchange. Use when Codex works with component-level IDX data rather than only board outlines or collaboration metadata.
---

# IDX Component Library

## Workflow

1. Use namespace-aware XML inspection to locate component item definitions and item instances.
2. Separate library definition data from placed component instance data.
3. Resolve electrical insertion point, body geometry, pin definitions, pin numbering/naming, and component transformations before visualizing or editing.
4. Preserve component properties such as value, tolerance, thermal data, material data, and padstack names when filtering or converting.
5. When creating component records, keep body and pin geometry consistent with the coordinate system and insertion point.
6. Validate with both semantic checks and visual checks: body dimensions, pin orientation, placement, padstack names, and property values.

## Reference

Read [references/component-library-notes.md](references/component-library-notes.md) for component modeling patterns.

The project reference document is `C:\Users\i00202914\Desktop\PSI5_IDXv4.5_Recommendation_Developer.pdf`.
