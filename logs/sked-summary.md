# SKED Dialogue Summary & Engineering Decisions Log

| Protocol Attribute | Value |
| :--- | :--- |
| **System Name** | Personal Knowledge & Learning Management System (PKLMS) |
| **Methodology** | SKED (Socratic Knowledge Elicitation & Documentation) |
| **Document Target** | Software Requirements Specification (`spec/srs.md`) |
| **Date of Elicitation** | September 17–18, 2026 |
| **Participants** | Human Expert / Student (Maksym Korniienko) & AI Systems Architect |
| **Log Location** | `logs/sked-summary.md` |

---

### 1. Overview & Objectives
This log records the formal knowledge elicitation session conducted according to the **SKED methodology** to establish the baseline Software Requirements Specification (SRS) for PKLMS. The dialogue followed an iterative Socratic cycle ($K^{(0)} \to K^{(1)} \to K^{(2)} \to K^*$) to eliminate ambiguities, uncover architectural blind spots, and validate engineering assumptions prior to document generation.

---

### 2. Initial Uncertainties & Blind Spots Identified (Step 1 & 2)

During the initial concept analysis, the following structural uncertainties were identified:
1. **System Delivery & Form Factor**: Whether the system was a CLI tool (common in prior SDD course assignments), a TUI, or a graphical web application.
2. **Decomposition Mechanics**: Whether educational goals were deconstructed manually by the learner, via pre-set templates, or using autonomous AI generative agents.
3. **Artifact Semantics & Verification Depth**: What constituted a valid "proof of work" (text only vs. multi-modal files), and whether the system performed semantic validation or syntactic existence checks.
4. **Task Completion Policy Ambiguity**: Reconciling the historical Git merge conflict recorded in `logs/git-gate.md` (`STRICT_ARTIFACT_MANDATORY` vs. `OPTIONAL_FOR_READING`) into a formal behavioral contract.
5. **Knowledge Base Lifecycle & Final Compilation**: Whether the final knowledge output was an exported monolithic PDF/document, or an ongoing interactive catalog.
6. **Wikilink Resolution Scope & Graph Rot**: How `[[wikilinks]]` resolved across multiple goals, and what happens when a referenced note is renamed.

---

### 3. Decisions Formulated by the Human Expert ($H$)

Across three rounds of Socratic inquiry, the Human Expert established the following definitive architectural decisions:
- **Web UI Architecture**: Selected a decoupled Single Page Application (**React + Vite + Tailwind CSS**) served as static assets directly by **FastAPI** on `http://localhost:8000`. Single-user, local-first, zero authentication.
- **Strict Tree Hierarchy**: Bounded tree depth to a maximum of **5 levels**. Established the **Strict Leaf Task Invariant**: tasks exist strictly at leaf positions ($\text{deg}^+(v) = 0$), and container nodes (`GOAL`, `MODULE`) cannot simultaneously own sub-modules and executable tasks.
- **Task Types & Policies (`TASK_TYPE_DEPENDENT`)**:
  - `READING`: `OPTIONAL` artifact; completed via manual acknowledgment checkbox; optional notes saved to vault.
  - `RESEARCH`: `MANDATORY` Markdown note $>100$ characters.
  - `PRACTICE`: `MANDATORY` code script, Git repo URL/commit hash, or Markdown summary ($>100$ characters).
  - `PROJECT / LAB`: `MANDATORY` attached project file/report ($>0$ bytes).
- **Post-Completion Mutability**: Notes remain editable after completion. If edited below character thresholds, status remains `COMPLETED` with a non-blocking soft warning.
- **Guarded Mandatory Artifact Deletion**: Deletion of the sole artifact of a mandatory task is protected by a confirmation prompt; upon deletion, status reverts to `IN_PROGRESS`.
- **Global Wikilinks & Atomic Refactoring**: Wikilinks support cross-goal references (`[[Goal / Note]]`). Renaming a note triggers an automated, transactional regex update across all stored Markdown notes.
- **Dual Mode Paradigm**: Workspace Mode for active execution ($P < 100\%$) transitions automatically to Knowledge Catalog Mode upon $100\%$ completion, hiding checkboxes and exposing an interactive reference wiki.
- **Export Packaging**: Tree structure is mirrored to local directories with zero-padded prefixes (`01_Module/`). Assets are normalized into `./assets/`, and relative links rewritten. Root `README.md` manifest is dynamically synthesized.

---

### 4. Model Assumptions Checked, Corrected, or Rejected

| Model Hypothesis / Assumption | Human Evaluation | Architectural Resolution & Impact |
| :--- | :---: | :--- |
| **Hypothesis 1: CLI Terminal Utility**<br>Assumed PKLMS would be implemented as a CLI tool following `retrieval_engine_spec` conventions. | **REJECTED** | Human explicitly mandated a modern, user-friendly **Web Interface (React SPA)** to support rich tree navigation and live Markdown editing. |
| **Hypothesis 2: Runtime Generative AI Summarizer**<br>Assumed the system would generate automatic lesson summaries using an LLM. | **REJECTED (MVP)** | Human mandated **Cognitive Sovereignty**: the human learner is the primary author. Generative AI is strictly excluded from MVP runtime and deferred to Phase 2. |
| **Hypothesis 3: Complex Text Concatenation on Goal Completion**<br>Assumed the system should stitch notes into a single compiled report. | **REJECTED** | Human mandated an **Interactive Knowledge Catalog**: the goal preserves its tree navigation, checkboxes are hidden, and notes remain independently readable/editable. |
| **Hypothesis 4: Automated Git Commits for Artifacts**<br>Assumed every artifact save would trigger an automated `git commit`. | **DEFERRED** | Human clarified that internal filesystem storage + ZIP export is sufficient for MVP; automated Git tracking is reserved for future versions. |
| **Hypothesis 5: Single-User Localhost Deployment**<br>Assumed zero-auth local web app. | **CONFIRMED** | Localhost execution accepted; no login screens, user accounts, or multi-tenant complexity for MVP. |
| **Hypothesis 6: SQLite WAL + Managed Filesystem Layout**<br>Assumed metadata in SQLite, files in `/storage/artifacts/`. | **CONFIRMED** | Accepted as optimal local-first storage architecture. |
| **Hypothesis 7: Soft Warning on Post-Completion Note Truncation**<br>Assumed short edits shouldn't revoke completed status without user consent. | **CONFIRMED** | Non-blocking inline warning displayed; task status preserved. |

---

### 5. Convergence Record ($\delta < \epsilon$)
At the conclusion of Round 3, all open questions regarding domain modeling, state machines, API routes, data contracts, and export packaging were resolved. The resulting consensus state $K^*$ was approved by the Human Expert, providing the complete foundation for `spec/srs.md`.
