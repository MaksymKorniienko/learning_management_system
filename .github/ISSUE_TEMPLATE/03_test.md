---
name: "3. Test (TEST)"
about: "Author automated unit, integration, or contract tests before code (TDD Red)"
title: "[TEST] [REQ-XXX]: "
labels: ["type: test", "status: todo"]
assignees: ""
---

### 1. Requirement & Scenario Traceability
- **Requirement ID**: `REQ-`
- **Scenario ID**: `SCEN-`
- **Target Test File**: `tests/unit/test_...py` or `tests/integration/test_...py`

### 2. Behavioral Contract Being Asserted
*Describe what behavior, invariant, or edge case this test enforces according to the SRS.*

### 3. Test Structure & BDD Alignment
- **Given**: Initial preconditions (in-memory SQLite DB state, model setup).
- **When**: Action or API call under test.
- **Then**: Expected assertions (return code, model state, exception raised).

### 4. TDD Red Verification
- [ ] Test implemented in `tests/`
- [ ] Test executes and **FAILS** for the expected reason (asserting yet-unimplemented behavior)
- [ ] Test failure output attached / documented
