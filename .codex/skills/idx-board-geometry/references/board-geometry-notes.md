# IDX Board Geometry Notes

Source basis: PSI5 IDX v4.5 Developer Recommendation sections on ECAD shape information, 2D geometry model, item shape, curve sets, cutouts, strata/layers, and implementation guidance for board modeling.

## Extraction Order

1. Parse XML and namespace map.
2. Identify units from the header and `UnitLength`.
3. Identify candidate board/panel items from `ItemType`, names, user properties, or relationships.
4. Follow product structure and shape associations instead of relying only on nearby XML order.
5. Resolve `ItemShape`, `ShapeDescription`, `ShapeElement`, `curve_set_2d`, and geometry elements.
6. Apply `transformation_2d` or `transformation_3d` when present.
7. Build typed output records with source IDs for traceability.

## Geometry Handling

- Treat lines, trimmed curves, ellipses, parabolas, offset curves, and composite curves distinctly until final rendering.
- Keep closed outlines explicit. Flag open curve chains when a board outline or cutout is expected to close.
- Store original coordinates and transformed coordinates when debugging imports.
- For visualization, convert units once at the boundary, not repeatedly in each geometry function.
- For Three.js previews, map 2D board coordinates onto the X/Y plane or X/Z plane consistently with the existing project camera.

## Board Semantics

Track these categories separately:

- Board outline or panel outline.
- Internal cutouts.
- Unsupported or partially plated passages.
- Mounting holes and component termination passages.
- Design/documentation layers and strata.
- Copper areas, keepouts, and constraints when present.

## Validation Checklist

- Bounding box matches expected board size.
- Main outline is closed and has the intended winding.
- Cutouts are inside the main outline.
- Hole diameters and positions remain in source units.
- Layer-specific entities are not accidentally rendered on all layers.
- Transformations do not mirror or rotate geometry unintentionally.
