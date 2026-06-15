---
name: idx-collaboration-workflow
description: Reason about IDX ECAD/MCAD collaboration workflows, baselines, incremental changes, history, ownership, acceptance, send/request messages, transaction state, and comparison between IDX files. Use when Codex needs to classify an IDX file as baseline/change data, preserve collaboration metadata, analyze component placement changes, board changes, replacements, ECO/ECR-style flows, or debug Creo/ECAD collaboration behavior in this project.
---

# IDX Collaboration Workflow

## Workflow

1. Inspect header and user properties first, especially `IDX_MODE`, `IDX_VERSION`, transaction state, creator/post processor, and systems.
2. Distinguish baseline data from change/collaboration data before editing or filtering.
3. Preserve `HistoryEntry`, `History`, actor/person, system scope, ownership, acceptance, and transaction metadata unless the task explicitly removes collaboration state.
4. When comparing two IDX files, compare IDs and domain semantics separately: board geometry, component item definitions, item instances, placements, properties, and history.
5. For component placement changes, resolve transformations and compare coordinates/rotation in normalized units.
6. For filtered output, keep enough metadata for downstream Creo/ECAD import to understand source, units, systems, and collaboration context.

## Reference

Read [references/collaboration-notes.md](references/collaboration-notes.md) for baseline/change handling patterns.

The project reference document is `C:\Users\i00202914\Desktop\PSI5_IDXv4.5_Recommendation_Developer.pdf`.
