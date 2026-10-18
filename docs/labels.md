# GitHub Labels Specification & Definitions

This reference defines the standardized label taxonomy for the PKLMS repository (`MaksymKorniienko/learning_management_system`).
Each label includes a hover description (maximum 100 characters) that displays as a tooltip in GitHub Issues, Pull Requests, and Project boards.

---

## 1. Status Labels (`status:*`)

| Label Name | Hex Color | Hover Description (Tooltip) | Meaning |
| :--- | :---: | :--- | :--- |
| `status: todo` | `#cfd3d7` | Pending task; requirements defined; ready to be picked up for development | Work not yet started |
| `status: in-progress` | `#0969da` | Active implementation, test authoring, or drafting is underway by the assignee | Work in progress |
| `status: in-review` | `#d4a72c` | Work completed; awaiting PR review, automated test pass, or quality audit | Under review / QA |
| `status: blocked` | `#d93f0b` | Work halted due to an unresolved upstream dependency, defect, or spec ambiguity | Blocked / Suspended |
| `status: done` | `#2da44e` | All acceptance criteria satisfied; tests passing; merged to main branch | Completed |

---

## 2. SDD Type Labels (`type:*`)

| Label Name | Hex Color | Hover Description (Tooltip) | Meaning |
| :--- | :---: | :--- | :--- |
| `type: specification` | `#1d76db` | Baseline system specification, domain schema, or API contract authored in SRS | Spec creation / update |
| `type: addendum` | `#5319e7` | Formal amendment, delta, or clarification to an approved baseline specification | Spec delta / RFC |
| `type: test` | `#e99695` | Automated unit, integration, or contract test asserting expected failure (TDD Red) | TDD Red test suite |
| `type: feature` | `#006b75` | Production code implementation satisfying passing test contracts (TDD Green) | Implementation code |
| `type: verification` | `#fbca04` | Internal technical quality check: static types, linting, test coverage (>= 90%) | Code & test quality check |
| `type: validation` | `#bfdadc` | User-centric acceptance: BDD scenarios, user journeys, cognitive invariants | Acceptance testing |
| `type: documentation` | `#0075ca` | User manuals, API Swagger schemas, README guides, and architecture documentation | Documentation |
| `type: gate` | `#b60205` | Formal blocking milestone checkpoint verifying prerequisite tickets before merge | Milestone quality gate |

---

## 3. Subsystem Domain Labels (`domain:*`)

| Label Name | Hex Color | Hover Description (Tooltip) | Related Requirements |
| :--- | :---: | :--- | :--- |
| `domain: tree` | `#c2e0c6` | Goal/Module/Task hierarchy, leaf invariants, and status roll-up logic | `REQ-TREE-xxx` |
| `domain: policy` | `#fef2c0` | Task completion policies (READING, RESEARCH, PRACTICE, PROJECT/LAB) | `REQ-POLICY-xxx` |
| `domain: artifact` | `#bfd4f2` | Artifact vault storage, MIME verification, size bounds, guarded deletion | `REQ-ARTIFACT-xxx` |
| `domain: wiki` | `#d4c5f9` | Bidirectional wikilinks, auto-refactoring, and SQLite FTS5 search | `REQ-WIKI-xxx` |
| `domain: export` | `#f9d0c4` | Portability engine, directory tree mirroring, and README manifest | `REQ-EXPORT-xxx` |
| `domain: ui` | `#e6cbf2` | React SPA, Workspace Mode, Knowledge Catalog Mode, and Markdown editor | `REQ-UI-xxx` |
