# IDX XML Notes

Source basis: PSI5 IDX v4.5 Developer Recommendation, plus this project's existing `.idx` files.

## Namespaces Seen In Project Files

Common IDX/EDMD namespaces:

- `foundation`: dataset, header, body, systems, units, items, item versions, item instances.
- `administration`: person and organization data.
- `annotation`: history and collaboration annotations.
- `computational`: computational or derived data.
- `d2`: 2D geometry model elements.
- `external`: digital file and external references.
- `grouping`: grouping/classification associations.
- `material`: material definitions and material properties.
- `pdm`: product structure, identifiers, item types.
- `property`: user properties, values, units, limits, ranges.

The PSI v4.5 text uses the term IDX in descriptions, while many schema class and XML names still contain EDMD.

## Inspection Priorities

For a new `.idx` file, record:

- XML root and namespace map.
- `Header` metadata, especially creator system, post processor, global unit, IDX mode, and IDX version.
- Counts for systems, persons, organizations, units, items, item versions, item instances, shapes, curves, transformations, properties, and history entries.
- IDs with duplicate detection.
- Top-level item types such as board, assembly, component, laminate, or other domain-specific values.
- User properties with keys scoped by `SystemScope` and `ObjectName`.

## Editing Rules

- Keep XML namespace prefixes consistent with the source file where practical.
- Preserve `id` values unless intentionally regenerating references.
- Update all dependent references if an object ID changes.
- Use explicit units. In project samples, `GlobalUnitLength` points to a `UnitLength` whose fundamental unit is `mm`.
- Avoid deleting unknown `UserProperty` entries; vendor-specific properties can drive Creo behavior.

## Common Failures

- Missing objects: unresolved ID references, filtered-out item versions, or geometry referenced through a shape relationship not followed by the parser.
- Incorrect dimensions: unit mismatch or unhandled transformation.
- Lost collaboration state: removed history, transaction, ownership, or IDX mode properties.
- XML parser errors: malformed file, truncated export, or an HTML/error response saved as `.idx`.
