---
name: "8. Gate (GATE)"
about: "Formal blocking quality gate checkpoint verifying prerequisite tickets before phase transition"
title: "[GATE] [MILESTONE-X]: "
labels: ["type: gate", "status: todo"]
assignees: ""
---

### 1. Gate Scope & Target Milestone
- **Milestone Name**: (e.g., Spec Approval Gate, Milestone 1 Implementation Gate, Release Gate)
- **Governing Protocol**: `docs/workflow.md#section-3`
- **Gate Protocol Artifact**: `logs/gate-...md`

### 2. Upstream Prerequisite Tickets
*All listed prerequisite tickets must be closed in `Done` state before this Gate can open.*
- [ ] Prerequisite 1: #
- [ ] Prerequisite 2: #
- [ ] Prerequisite 3: #

### 3. Formal Gate Criteria Verification
- [ ] **Specification Consistency**: 100% of implemented capabilities are specified in `spec/srs.md`.
- [ ] **Traceability Integrity**: Zero orphaned code or unlinked requirements.
- [ ] **Quality Invariant**: Test coverage $\ge 90\%$, zero static analysis or type defects.
- [ ] **Audit Report**: Formal gate protocol document compiled and committed to `logs/`.

### 4. Gate Sign-off Verdict
- [ ] **GATE PASSED**: Transition to subsequent milestone approved.
- [ ] **GATE REJECTED**: Blocker defects identified; transition halted.
