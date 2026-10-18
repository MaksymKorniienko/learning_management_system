---
name: "4. Feature (FEAT)"
about: "Implement minimal production code to satisfy failing tests (TDD Green)"
title: "[FEAT] [REQ-XXX]: "
labels: ["type: feature", "status: todo"]
assignees: ""
---

### 1. Traceability & Prerequisite Tests
- **Requirement ID**: `REQ-`
- **Linked Failing Test Ticket(s)**: Fixes # (or `tests/test_...py`)
- **Target Source Modules**: `src/backend/...` or `src/frontend/...`

### 2. Implementation Scope
*Describe the minimal production logic required to turn the failing test green without introducing out-of-scope behaviors.*

### 3. Architecture & Design Alignment
- Layer: (Router / Service / Model / Repository / UI Component)
- Design Invariant: (e.g., Strict Leaf Task, ACID Transaction, Zero-Telemetry)

### 4. Definition of Done Checklist
- [ ] Minimal code implemented in `src/`
- [ ] All linked `TEST` tickets turn **GREEN** (tests pass)
- [ ] Zero regression across existing test suites
- [ ] Code formatted and statically typed (`mypy`, `ruff`)
