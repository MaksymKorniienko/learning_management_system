# SDD Development Workflow & Project Governance Protocol

| Parameter | Specification Details |
| :--- | :--- |
| **System** | Personal Knowledge & Learning Management System (PKLMS) |
| **Methodology** | Specification-Driven Development (SDD) with Mandatory TDD |
| **Governing Spec** | [`spec/srs.md`](../spec/srs.md) (v0.2.0-draft) |
| **Document Target** | `docs/workflow.md` |
| **Issue Tracker** | GitHub Issues + GitHub Projects (v2) |

---

## 1. Overview & Principles

This document establishes the official development workflow and issue lifecycle for PKLMS. Development is governed by **Specification-Driven Development (SDD)**, enforcing two fundamental invariants:
1. **Specification as Single Source of Truth**: No feature is implemented without prior formal specification in `spec/srs.md`.
2. **Mandatory Test-Driven Development (TDD)**: No production code is accepted without automated test coverage failing first (Red-Green-Refactor).
3. **Unbroken Traceability**: Every work item must link back to an approved Requirement ID (`REQ-XXX`) and Acceptance Scenario (`SCEN-XXX`).

---

## 2. Status State Machine & Workflow Transitions

All work items in GitHub Issues and the GitHub Project Board transition through five distinct states:

```
                  ┌──────────────────────────────────────────────┐
                  │                                              │
                  ▼                                              │
 ┌───────────┐         ┌───────────────┐         ┌───────────┐   │
 │   To Do   │ ──────> │  In Progress  │ ──────> │ In Review │ ──┤
 └─────┬─────┘         └───────┬───────┘         └─────┬─────┘   │
       │                       │                       │         │
       │ (Dependency)          │ (Blocker)             │         │
       ▼                       ▼                       ▼         │
 ┌───────────────────────────────────────────────────────────┐   │
 │                          Blocked                          │   │
 └───────────────────────────────────────────────────────────┘   │
                               │ (Blocker resolved)              │
                               ▼                                 │
                         (Previous State)                        │
                                                                 │ (Passed)
                                                                 ▼
                                                           ┌───────────┐
                                                           │   Done    │
                                                           └───────────┘
```

### Detailed Status Definitions

| Status | SDD Meta-State | Operational Criteria | Entry Condition | Exit / Done Condition |
| :--- | :--- | :--- | :--- | :--- |
| **`To Do`** | **Pending** | The ticket is fully formulated, assigned an SDD Type, and linked to a Requirement ID (`REQ-XXX`). Work is ready to be picked up. | Ticket created and backlog-prioritized. | Assignee starts work and branches from `main`. |
| **`In Progress`** | **Active** | Active drafting or coding is underway by the designated assignee. | Branch created (`feat/`, `test/`, `spec/`), first commit made. | Work complete; test suites or draft ready for review; PR opened. |
| **`In Review`** | **Under Review** | The work is undergoing quality gates: PR review, automated CI tests running, coverage calculation, or Gate audit. | Pull Request opened against `main`; CI triggered. | All automated checks pass ($\ge 90\%$ test coverage), reviews approved, gate signed off. |
| **`Done`** | **Completed** | The task's Definition of Done is fully met. Work is merged into the `main` branch. | PR merged or Gate artifact accepted. | Ticket closed. |
| **`Blocked`** | **Suspended** | Work cannot continue due to an external blocker, upstream dependency, or open specification conflict. | Unresolved dependency or conflict flagged. | Blocker removed; returns to `To Do` or `In Progress`. |

---

## 3. SDD Ticket Types & Lifecycle

Every task created in GitHub Issues MUST be assigned exactly one primary SDD Ticket Type:

```
                  ┌──────────────────────┐
                  │ 1. Specification     │
                  └──────────┬───────────┘
                             │ (Baseline established)
                             ▼
 ┌───────────────┐        ┌──────────────────────┐
 │ 2. Addendum   │───────>│ 8. Gate (Spec-Gate)  │
 └───────────────┘        └──────────┬───────────┘
                             │
            ┌────────────────┴────────────────┐
            ▼                                 ▼
 ┌──────────────────────┐          ┌──────────────────────┐
 │ 3. Test (TDD Red)    │          │ 7. Documentation     │
 └──────────┬───────────┘          └──────────────────────┘
            │ (Failing tests written)
            ▼
 ┌──────────────────────┐
 │ 4. Feature (TDD Green│
 └──────────┬───────────┘
            │
            ├─────────────────────────┐
            ▼                         ▼
 ┌──────────────────────┐  ┌──────────────────────┐
 │ 5. Verification      │  │ 6. Validation        │
 │ (Static / Unit / Cov)│  │ (BDD / User Scenarios│
 └──────────┬───────────┘  └──────────┬───────────┘
            │                         │
            └────────────┬────────────┘
                         ▼
             ┌──────────────────────┐
             │ 8. Gate (Milestone)  │
             └──────────────────────┘
```

### Ticket Type Taxonomy

| # | Type Name | Label | SDD Phase & Responsibility | Deliverable / Output Artifact |
| :-: | :--- | :--- | :--- | :--- |
| **1** | **Specification** | `type: specification` | Authoring baseline system specifications, domain schemas, API contracts, or DDL definitions before any code is written. | Markdown updates in `spec/srs.md`, data contracts in Pydantic/OpenAPI. |
| **2** | **Addendum** | `type: addendum` | Formal amendments, deltas, or clarifications to an already approved baseline specification (handling newly discovered edge cases). | Specification delta commit, version increment (e.g., `v0.2.0` $\to$ `v0.2.1`), changelog. |
| **3** | **Test** | `type: test` | Authoring automated unit, integration, or contract tests *before* production code (TDD Red phase). Must assert expected failure. | Test suites in `tests/unit/` or `tests/integration/` encoding `SCEN-xxx`. |
| **4** | **Feature** | `type: feature` | Implementing minimal, clean production code to satisfy passing tests (TDD Green phase). | Code modules in `src/backend/app/` or `src/frontend/src/`. |
| **5** | **Verification** | `type: verification` | *"Did we build the system right?"* Internal technical quality checks: static analysis, type checking (`mypy`), linting (`ruff`), and code coverage ($\ge 90\%$). | Coverage reports (`htmlcov/`), linting logs, static analysis passing. |
| **6** | **Validation** | `type: validation` | *"Did we build the right system?"* User-centric validation: executing end-to-end BDD scenarios, user journey testing, and cognitive sovereignty invariants. | Acceptance test run reports, BDD verification logs, validation checklists. |
| **7** | **Documentation** | `type: documentation` | Authoring user manuals, API Swagger documentation, deployment guides, or architecture diagrams. | Files in `docs/`, inline docstrings, README updates. |
| **8** | **Gate** | `type: gate` | Formal milestone checkpoints that block progression until all prerequisite tickets are validated and closed. | Gate audit report (e.g., `logs/spec-audit.md`, `logs/gate-m1.md`). |

---

## 4. Traceability Chain & Ticket Naming Standard

### 4.1 Traceability Formula

Every ticket MUST declare its position in the unbroken traceability chain:

$$\text{Requirement ID (REQ-XXX)} \longrightarrow \text{Scenario ID (SCEN-XXX)} \longrightarrow \text{Test ID (TEST-XXX)} \longrightarrow \text{PR / Commit}$$

### 4.2 Standard Ticket Title Format

```text
[<TYPE>] [<REQ-ID>]: <Concise Imperative Description>
```

**Examples**:
- `[SPEC] [REQ-TREE-001]: Define recursive status roll-up contract and DDL constraints`
- `[TEST] [REQ-POLICY-002]: Add failing unit tests for RESEARCH note character threshold`
- `[FEAT] [REQ-POLICY-002]: Implement PolicyService length validator excluding scaffolding`
- `[VERIF] [MILESTONE-1]: Verify backend test coverage reaches >= 90% and static types pass`
- `[GATE] [MILESTONE-1]: Audit and sign off Phase 1 Backend Core Implementation`

---

## 5. Definition of Done (DoD)

A ticket can only transition to **`Done`** when the following checklist is completely satisfied:

- [ ] **Traceability**: Linked to corresponding Requirement ID (`REQ-XXX`) in `spec/srs.md`.
- [ ] **Tests Pass (TDD Green)**: All relevant automated tests pass deterministically.
- [ ] **Coverage Invariant**: Line and branch coverage for modified modules is $\ge 90\%$.
- [ ] **Static Quality**: Code passes `ruff` (linter) and `mypy` (strict type checks) with zero errors.
- [ ] **Documentation**: Any schema, API, or behavioral change is documented in `spec/srs.md` or `docs/`.
- [ ] **Branch Merged**: PR cleanly merged into `main` with squash or rebase commit.
