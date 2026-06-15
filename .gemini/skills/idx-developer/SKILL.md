---
name: idx-developer
description: Assists with parsing, generating, and validating EDMD/IDX XML files for ECAD/MCAD collaboration (Prostep IVIP PSI5 v4.5). Use when generating IDX exports, parsing board baselines, or implementing SendInformation/SendChanges protocols.
---

# IDX Developer Skill

This skill provides expert guidance on working with the Interdomain Design eXchange (IDX) XML format used for ECAD/MCAD collaboration, based on the prostep ivip PSI 5 (Version 4.5) recommendation.

## Core Workflows

### 1. Generating IDX Files (Exporting)
When generating IDX files from an application:
*   Ensure the root is always `<pdm:EDMDDataSet>`.
*   Maintain the separation between `<foundation:Item>` (the component definition) and `<pdm:ItemInstance>` (the specific placement on the board).
*   For newly added components in an existing board baseline, ensure they contain a valid `<pdm:Shape>` reference or synthesize a valid `<pdm:CurveSet2d>` with an upper and lower bound thickness.
*   Modifications should either update existing `<pdm:Transformation>` properties (tx, ty, tz) within a baseline, or use the `SendChanges` protocol with `NewItem` and `PredecessorItem` structures for strict collaboration loops.

### 2. Parsing IDX Files (Importing)
When reading IDX XML files:
*   Account for various namespaces (e.g., `pdm:`, `foundation:`, `property:`).
*   Extract part definitions from `<foundation:Item id="...">` where `ItemType` is `single`.
*   Extract placement data from `<pdm:ItemInstance>` where the parent `Item` is an `assembly` (like the PCB board itself).
*   Identify whether components are placed on the TOP or BOTTOM of the PCB by checking the `<pdm:AssembleToName>` node inside the `ItemInstance`.
*   Note that MCAD tools (like Creo) typically export using a Z-Up coordinate system.

## References

For deeper architectural guidance on the IDX schema, protocol rules, and shape definitions, read the specification reference:
*   [IDX v4.5 Specification Reference](references/idx_v45_spec.md)
