# IDX Component Library Notes

Source basis: PSI5 IDX v4.5 Developer Recommendation sections on standardized library components, parameterized library components, 3D master parts, body, pin, thermal properties, value/tolerance properties, and padstack names.

## Component Data Separation

Keep these layers distinct:

- Library component definition: reusable component identity and geometry.
- Body definition: component package body dimensions and shape.
- Pin definition: pin count, names, numbers, type, bend/angle parameters, and positions.
- Placed instance: transformation and board-side placement.
- Properties: electrical value, tolerance, material, thermal behavior, padstack names, and vendor-specific user properties.

## Modeling Guidelines

- Start from the electrical insertion point and coordinate system.
- Model bodies and pins relative to the insertion point.
- Preserve pin numbering and names exactly; downstream systems may rely on them.
- Keep padstack names when present, especially for ECAD import/export round trips.
- Use explicit units and avoid implicit scale conversions.

## Visualization Guidelines

- Render bodies and pins in separate visual layers or colors when debugging.
- Show insertion point and local axes for placement issues.
- For pin rows, verify offsets, spacing, and orientation before blaming transformations.
- In Three.js previews, use simple primitives for bodies and pins unless exact geometry is needed.

## Common Failure Modes

- Component appears offset: insertion point or instance transformation is mishandled.
- Pins mirrored or rotated: local coordinate system or rotation order is wrong.
- Properties lost after filtering: user properties or property associations were removed.
- ECAD import loses pad information: padstack names or termination passage data were not preserved.
