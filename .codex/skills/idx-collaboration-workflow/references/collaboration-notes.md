# IDX Collaboration Notes

Source basis: PSI5 IDX v4.5 Developer Recommendation use cases and IDX protocol sections.

## Collaboration Concepts

IDX supports ECAD/MCAD collaboration across board baseline definition, placement under mechanical or electrical constraints, component changes, placement changes, component replacement, and panelization review.

Treat these as collaboration records, not just geometry edits:

- Actor/system/person information.
- Baseline or incremental change context.
- History entries and comments.
- Ownership and acceptance state.
- Transaction state and message purpose.
- System-scoped user properties.

## File Comparison Priorities

When comparing baseline and changed IDX files:

- Header mode/version and source system.
- Units.
- Added/removed/changed item definitions.
- Added/removed/changed item instances.
- Placement transformations.
- Board outline and cutout changes.
- Component properties, value/tolerance, material, and thermal properties.
- History entries and acceptance metadata.

## Preservation Rules

- Keep IDs stable when an element is unchanged.
- Keep references valid after filtering or transforming files.
- Do not remove unknown vendor-specific user properties by default.
- Preserve enough context for a self-contained message when downstream import requires it.

## Diagnostics

If Creo or ECAD import rejects a file, inspect:

- Whether the file is a baseline or change message expected by the receiver.
- Missing referenced systems, persons, units, histories, items, shapes, or transformations.
- Duplicate IDs.
- Removed history or transaction state.
- Unit or transformation changes that make placements appear invalid.
