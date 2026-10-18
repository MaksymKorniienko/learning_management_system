---
name: "5. Verification (VERIF)"
about: "Internal technical quality verification: coverage check, static analysis, linting"
title: "[VERIF] [MILESTONE-X]: "
labels: ["type: verification", "status: todo"]
assignees: ""
---

### 1. Verification Scope & Target Milestone
- **Milestone / Subsystem**: (e.g., Milestone 1 Backend Core, Tree Engine)
- **Target Source Modules**: `src/`

### 2. Quality Verification Dimensions
*Did we build the system right? Verify internal architectural conformance.*

- [ ] **Test Coverage Invariant**: Overall test coverage is $\ge 90\%$ (`pytest --cov=src --cov-report=term-missing`).
- [ ] **Static Type Analysis**: `mypy src tests` passes with zero type errors.
- [ ] **Linter & Style Standards**: `ruff check .` passes with zero violations.
- [ ] **Schema & Contract Conformance**: SQLite DDL and Pydantic v2 schemas match `spec/srs.md` Section 10 exactly.

### 3. Verification Evidence & Metrics
*Paste command execution summaries, test runner output, or coverage tables.*

### 4. Verdict & Status
- [ ] **PASSED**: All quantitative quality criteria met without exceptions.
- [ ] **FAILED**: Defects or coverage deficits identified (issue filed).
