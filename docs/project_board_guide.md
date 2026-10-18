# GitHub Projects (v2) Setup & Configuration Guide

This guide details how to configure GitHub Projects (v2) for the PKLMS repository (`MaksymKorniienko/learning_management_system`) to establish our SDD Kanban board, traceability views, and project definitions panel.

---

## 1. Creating the Project Board

1. In GitHub, navigate to **[Projects](https://github.com/MaksymKorniienko/learning_management_system/projects)** tab (or your user profile `https://github.com/users/MaksymKorniienko/projects`).
2. Click **"New project"**.
3. Select **"Board"** template and click **"Create"**.
4. Name the project: `PKLMS: SDD Implementation Hub`.
5. Link repository: Under project settings, link `learning_management_system`.

---

## 2. Custom Fields Configuration

Under project settings (`...` $\to$ **Settings** $\to$ **Custom fields**), configure the following fields:

| Field Name | Field Type | Options / Format | Purpose |
| :--- | :---: | :--- | :--- |
| **`Status`** | Single Select | • `To Do` (Gray)<br>• `In Progress` (Blue)<br>• `In Review` (Yellow)<br>• `Done` (Green)<br>• `Blocked` (Red) | Workflow state machine |
| **`Type`** | Single Select | • `Specification`<br>• `Addendum`<br>• `Test`<br>• `Feature`<br>• `Verification`<br>• `Validation`<br>• `Documentation`<br>• `Gate` | SDD lifecycle classification |
| **`Req ID`** | Text | e.g., `REQ-TREE-001`, `REQ-POLICY-002` | Unbroken requirement traceability |
| **`Subsystem`** | Single Select | • `TREE`<br>• `POLICY`<br>• `ARTIFACT`<br>• `WIKI`<br>• `EXPORT`<br>• `UI` | Functional domain partitioning |

---

## 3. Recommended Views

Configure three specialized tabs at the top of your project:

### View 1: 📋 SDD Kanban Board
- **Layout**: Board
- **Column by**: `Status`
- **Visible fields**: `Title`, `Assignees`, `Type`, `Req ID`, `Labels`
- **Filter**: `is:open` (or include closed in `Done`)

### View 2: 🔍 Traceability Table
- **Layout**: Table
- **Group by**: `Req ID` (or `Type`)
- **Columns**: `Title`, `Status`, `Type`, `Req ID`, `Subsystem`, `Assignees`
- **Purpose**: Verify that every requirement has associated `TEST`, `FEAT`, and `VERIF` tickets.

### View 3: 🚦 Quality Gates & Milestones
- **Layout**: Table or Roadmap
- **Filter**: `Type: Gate` or `is:issue`
- **Group by**: `Milestone`
- **Purpose**: Track blocking gates before phase transitions.

---

## 4. Project README Content (Copy & Paste into GitHub Project Readme)

In GitHub Projects (v2), click the **📖 Readme** button at the top-right header and paste the following markdown text:

```markdown
# 🏛️ PKLMS SDD Project Execution Hub

Welcome to the **Personal Knowledge & Learning Management System (PKLMS)** implementation board.
This project is engineered under **Specification-Driven Development (SDD)** with mandatory **TDD**.

- **Approved SRS (Source of Truth)**: [`spec/srs.md`](https://github.com/MaksymKorniienko/learning_management_system/blob/main/spec/srs.md)
- **Workflow & Rules**: [`docs/workflow.md`](https://github.com/MaksymKorniienko/learning_management_system/blob/main/docs/workflow.md)
- **Label Taxonomy**: [`docs/labels.md`](https://github.com/MaksymKorniienko/learning_management_system/blob/main/docs/labels.md)

---

### 🚦 Status Definitions

| Status | Meaning & Exit Criteria |
| :--- | :--- |
| **To Do** | Pending work; requirement specified (`REQ-XXX`); ready for assignment. |
| **In Progress** | Active coding/testing on feature branch (`feat/`, `test/`). |
| **In Review** | PR open; automated tests passing; peer review / gate audit underway. |
| **Blocked** | Halted due to an unresolved upstream dependency or spec conflict. |
| **Done** | Merged into `main`; >= 90% test coverage; traceability satisfied. |

---

### 🏷️ SDD Ticket Types

1. **Specification (`SPEC`)**: Baseline SRS rules, schemas, and models.
2. **Addendum (`ADD`)**: Formal amendments or clarifications to approved baseline.
3. **Test (`TEST`)**: Failing unit/integration test suites (TDD Red phase).
4. **Feature (`FEAT`)**: Minimal production code satisfying tests (TDD Green phase).
5. **Verification (`VERIF`)**: Static analysis, linting, test coverage (>= 90%).
6. **Validation (`VALID`)**: User-centric acceptance and BDD scenario execution.
7. **Documentation (`DOC`)**: Architecture docs, guides, and API schemas.
8. **Gate (`GATE`)**: Formal blocking milestone audit and sign-off.

---

### 🔗 Traceability Invariant
`REQ-XXX` (SRS) ➔ `SCEN-XXX` (BDD) ➔ `TEST-XXX` (pytest) ➔ `FEAT` (src code) ➔ `GATE` (Audit)
```
