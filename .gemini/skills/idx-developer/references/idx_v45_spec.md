# IDX (Interdomain Design eXchange) v4.5 Developer Reference

This document summarizes the core architectural principles, schema elements, and protocols described in the prostep ivip Recommendation PSI 5 "ECAD/MCAD Collaboration Developer Recommendation" (Version 4.5).

## Core Concepts

*   **EDMD (Electrical Design Mechanical Design)**: Often used interchangeably with IDX in schema namespaces.
*   **IDX**: Interdomain Design eXchange format. XML-based standard for ECAD/MCAD collaboration.
*   **Item (`EDMDItem`)**: The basic element describing a product (part or assembly) or a geometric element. It describes a *defined state* of an element.
*   **ItemInstance (`EDMDItemInstance`)**: Represents the placement and usage of an Item within an assembly (e.g., a specific resistor placed on a board).
*   **Transformation (`EDMDTransformation`)**: Defines the 2D or 3D location and orientation of an `ItemInstance` relative to its parent.

## The Data Model (IDX Schema)

The schema is divided into namespaces (packages):
*   `foundation`: Base types (`EDMDItem`, `EDMDItemInstance`, `EDMDSystem`).
*   `pdm`: Product structure (`EDMDAssemblyComponent`, `EDMDStratum`, `EDMDShapeElement`).
*   `geometry.d2` / `geometry.d3`: Geometric definitions (`EDMDCurveSet2d`, etc.).
*   `property`: User and system properties.
*   `computational`: Message envelopes (`SendInformation`, `SendChanges`).

### Representing Shapes

Shapes in IDX are built using `EDMDItemShape`. 
*   A 2D shape is commonly represented using `EDMDCurveSet2d`, combining points, lines, arcs, etc.
*   **Bounding Box**: Each shape has a bounding box definition.
*   **Top/Bottom Placement**: Indicated by the `AssembleToName` node under `ItemInstance`, usually set to "TOP" or "BOTTOM".

### Standardized 3D Master Models

For parameterized library components (Package `3d_master_parts`), components are defined using generic geometric bodies (Basic, Restricted_Area, Cut_Out) and pins (types L, I, Z, C).
*   **Coordinate System**: Clockwise Cartesian (X, Y, Z). Origin is typically in the middle of the bottom surface of the body.
*   **Z-Up vs Y-Up**: Creo (MCAD) generally expects Z-up.

## IDX Protocol & Messages

Collaboration is achieved by exchanging specific XML message structures.

### 1. `SendInformation`
Used to send the initial baseline or complete information about items. 
*   Root element: `EDMDDataSet`.
*   Processing: Receiver iterates over items, creates missing ones, updates existing ones (PackageName, ItemInstance lists, Shape, Accept-Status).

### 2. `SendChanges`
Used to propose modifications to a baseline.
*   Includes a list of changes (`EDMDChange` or subtypes).
*   Refers to `NewItem` (the new state) and `PredecessorItem` (the old state).
*   Can include `DeletedInstanceName` for components that were removed.
*   Processing: The receiver applies the delta. Unmentioned attributes remain as they were in the `PredecessorItem`.

### 3. `RequestForInformation`
Used by a system to request details for an "item stub" (an item where only the identifier is known).

### Self-Contained Messages
A self-contained document (flagged `IsSelfContained` at `EDMDHeader`) has no external links to other documents via item stubs. All known identifiers and attributes of an item must be included.

## System Context & Designators

Since different CAD/PLM systems use different IDs for the same part, IDX uses `EDMDDesignator` inside `EDMDItem`.
*   An Item can have multiple designators, each tied to a specific `EDMDSystem` context (e.g., `ECAD@machine2`, `MCAD@machine1`).
*   When receiving a file, systems use these designators to map the IDX component back to their internal database IDs.
