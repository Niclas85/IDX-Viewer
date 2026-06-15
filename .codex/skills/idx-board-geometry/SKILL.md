---
name: idx-board-geometry
description: Extract, interpret, visualize, or debug IDX board geometry and 2D shape data. Use when Codex works with IDX board outlines, panels, cutouts, holes/passages, layers/strata, copper areas, curves, line/arc/ellipse geometry, curve_set_2d, item_shape, transformations, units, or conversion into SVG, canvas, Three.js, Creo ECAD import previews, or geometry filtering in this project.
---

# IDX Board Geometry

## Workflow

1. Use `idx-xml-inspect` first when the file structure is unknown.
2. Find the board or panel item, then follow its item version, item instance, item shape, and geometry references.
3. Resolve length units before computing coordinates. Do not assume meters; project samples use millimeters.
4. Resolve transformations before rendering or comparing geometry.
5. Preserve semantic categories: board outline, cutouts, holes/passages, layers/strata, copper areas, and documentation features should not be flattened into one undifferentiated curve list unless the caller asks for a visual-only preview.
6. Validate output visually and numerically: bounding box, closed outlines, curve continuity, orientation, and layer assignment.

## Reference

Read [references/board-geometry-notes.md](references/board-geometry-notes.md) for extraction and visualization patterns.

The project reference document is `C:\Users\i00202914\Desktop\PSI5_IDXv4.5_Recommendation_Developer.pdf`.
