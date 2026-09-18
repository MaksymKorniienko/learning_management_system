# Personal Knowledge & Learning Management System (PKLMS)

[![Specification-Driven Development](https://img.shields.io/badge/Discipline-SDD%20%7C%20Spec--Driven-blue.svg)](spec/srs.md)
[![Testing Discipline](https://img.shields.io/badge/Testing-Mandatory%20TDD%20(%E2%89%A590%25%20Coverage)-success.svg)](spec/srs.md#13-testing-strategy--quality-gates)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI%20%2B%20Pydantic%20v2-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![SQLite FTS5](https://img.shields.io/badge/Storage-SQLite3%20WAL%20%2B%20FTS5-003B57.svg?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![React 18](https://img.shields.io/badge/Frontend-React%2018%20%2B%20Vite%20%2B%20Tailwind-61DAFB.svg?logo=react&logoColor=black)](https://react.dev/)
[![Local-First](https://img.shields.io/badge/Privacy-100%25%20Local--First%20%7C%20Zero--Telemetry-purple.svg)](spec/srs.md#12-problem-statement--cognitive-sovereignty)

> **A deterministic, local-first learning execution hub bridging task discipline and persistent knowledge synthesis.**

---

## 📌 Executive Summary

Modern self-directed digital learning suffers from a widespread cognitive pathology: the **illusion of competence**. Learners consume massive volumes of articles, video lectures, and tutorials without producing verifiable proof of work. Because traditional task managers treat tasks as disposable checklist items and personal knowledge management (PKM) tools lack execution discipline, acquired knowledge rapidly degrades according to Ebbinghaus's forgetting curve.

**PKLMS** resolves this failure by enforcing **Cognitive Sovereignty**:
- **Goal Decomposition**: Deconstructs high-level curricula into a strict hierarchical tree ($\text{depth} \le 5$) down to atomic leaf tasks.
- **Evidence-Gated Completion**: Eliminates mindless checkbox ticking by requiring concrete, task-type-dependent artifacts (synthesis notes, scripts, repo commits, lab archives) before state transitions are permitted.
- **Persistent Knowledge Compounding**: Completed tasks automatically index into a bidirectional, searchable personal knowledge vault equipped with `[[wikilinks]]`, atomic link refactoring, tag taxonomies, and embedded SQLite FTS5 full-text search.
- **Dual Operating Modes**: Automatically shifts from an execution-focused **Workspace Mode** to an interactive, review-ready **Knowledge Catalog Mode** when a curriculum reaches 100% completion.
- **Standardized CommonMark Export**: Offers one-click, deterministic export into a clean mirrored directory tree with relative `./assets/` normalization and root `README.md` curriculum manifests compatible with Obsidian, VS Code, and GitHub.

The entire system is governed under **Specification-Driven Development (SDD)** with the formal specification at [`spec/srs.md`](spec/srs.md) acting as the single source of truth.

---

## 🏛️ System Architecture

PKLMS is engineered as a lightweight, single-process, local-first desktop web system. The frontend is bundled and statically served by the FastAPI application, requiring zero cloud services, external database servers, or multi-process orchestrators.

```
+-------------------------------------------------------------------------+
|                              CLIENT LAYER                               |
|       React 18 SPA + Vite + Tailwind CSS + Lucide Icons + EasyMDE       |
+-------------------------------------------------------------------------+
                                    |
                          REST API / JSON (HTTP)
                                    v
+-------------------------------------------------------------------------+
|                             BACKEND ENGINE                              |
|          Python 3.11+ / FastAPI / Pydantic v2 / Uvicorn Server          |
|  +-------------------------------------------------------------------+  |
|  | Routers: /goals, /nodes, /tasks, /artifacts, /search, /export     |  |
|  | Services: TreeService, PolicyService, WikiService, ExportService  |  |
|  +-------------------------------------------------------------------+  |
+-------------------------------------------------------------------------+
         |                                                 |
         v                                                 v
+---------------------------+             +-------------------------------+
|     RELATIONAL / FTS5     |             |      MANAGED FILE SYSTEM      |
|    SQLite 3 (WAL Mode)    |             |       /storage/artifacts/     |
|   Metadata, Nodes, FTS5   |             |   Raw .md, .py, .png, .pdf    |
+---------------------------+             +-------------------------------+
```

### Component Breakdown

| Layer / Subsystem | Technology | Responsibility |
| :--- | :--- | :--- |
| **Backend Core** | FastAPI (Python 3.11+) | High-performance async REST API, dependency injection, and Pydantic v2 data contract enforcement. |
| **Database Engine** | SQLite 3 (WAL Mode) | Embedded relational persistence with ACID guarantees and zero external server dependencies. |
| **Search Engine** | SQLite FTS5 Virtual Tables | Sub-millisecond full-text lexical search with Unicode61 diacritic-insensitive tokenization. |
| **Artifact Vault** | Local Filesystem (`/storage/artifacts/`) | Sandboxed file persistence, MIME whitelisting, size bounding, and path sanitization. |
| **Frontend Client** | React 18 + Vite + Tailwind CSS | Responsive SPA with dual view paradigms (Workspace vs. Knowledge Catalog) and live Markdown editing. |

---

## 🔑 Core Features & Invariants

### 1. Hierarchical Tree Decomposition
* **Strict Node Typing**: Nodes are strictly classified into `GOAL` (root container), `MODULE` (intermediate container), and `TASK` (atomic work unit).
* **Strict Leaf-Level Tasks (`Invariant 6.2`)**: Tasks exist strictly as leaves ($\text{deg}^+(v) = 0$). Container nodes cannot mix sub-modules and direct tasks.
* **Bounded Depth (`Invariant 6.3`)**: Tree depth is strictly constrained: $\text{depth}(v) \le 5$.
* **Deterministic Status Roll-up**: Parent progress $P(v)$ is computed bottom-up automatically. When $P(v_{\text{root}}) = 100\%$, the Goal transitions automatically to **Knowledge Catalog Mode**.

### 2. Task-Type-Dependent Completion Policies
Completion criteria are strictly enforced by the backend policy engine before granting the `COMPLETED` state:

| Task Type | Policy Key | Mandatory Artifact / Verification Criteria |
| :--- | :--- | :--- |
| **`READING`** | `OPTIONAL_ARTIFACT` | May complete immediately via "Acknowledge" button; notes saved if provided. |
| **`RESEARCH`** | `STRICT_MANDATORY_NOTE` | Requires Markdown note $> 100$ characters (excluding whitespace and markdown syntax). Note editor provides structured scaffolding (`## Summary`, `## Insights`). |
| **`PRACTICE`** | `STRICT_MANDATORY_CODE_OR_REPO` | Requires an uploaded code file (`.py`, `.ts`, `.sql`, etc.), a valid Git URL/commit SHA regex match, or a descriptive summary note ($>100$ chars). |
| **`PROJECT/LAB`** | `STRICT_MANDATORY_PROJECT_ARTIFACT` | Requires an attached project archive (`.zip`), document report (`.pdf`, `.md`), or compiled summary file with $\text{size} > 0$ bytes. |

> [!NOTE]
> **Guarded Deletion**: Deleting the sole qualifying artifact of a completed mandatory task prompts an explicit confirmation dialog and automatically rolls back task status to `IN_PROGRESS` and recalculates parent tree progress.
> **Post-Completion Editing**: Subsequent edits dropping note length below 100 characters retain `COMPLETED` status but display an inline non-blocking advisory banner.

### 3. Knowledge Graph, Wikilinks & FTS5 Search
* **Bidirectional Wikilinks**: Supports local `[[Note Title]]` and cross-goal `[[Goal / Note Title]]` links with automatic backlink extraction.
* **Atomic Link Refactoring**: Modifying a node's title automatically and transactionally scans and rewrites all referencing `[[wikilinks]]` across the database and stored Markdown files.
* **SQLite FTS5 Full-Text Search**: Sub-50ms search queries supporting prefix searches (`distrib*`), exact phrases (`"consensus protocol"`), and boolean operators.
* **Relational Tagging**: Extracts `#tags` from Markdown content and supports faceted tag cloud filtering.

### 4. Dual View Modes
* **Workspace Mode ($P < 100\%$)**: Active execution interface equipped with tree modification controls, task completion buttons, upload drops, and live editors.
* **Knowledge Catalog Mode ($P = 100\%$)**: Clutter-free synthesis view where checkboxes are hidden, presenting the completed goal as an interactive, connected reference manual.

### 5. Deterministic Export Engine
* **Clean Tree Mirroring**: Exports goals into zero-padded ordered directories (`01_Module/01_Task_note.md`).
* **Asset Normalization**: Isolates images and PDFs into localized `./assets/` folders and rewrites Markdown links to relative paths (`![](./assets/...)`).
* **Manifest Generation**: Synthesizes a root `README.md` containing goal metadata and a hyperlinked Table of Contents. 100% compatible with Obsidian, VS Code, and GitHub.

---

## 📂 Repository Layout

This repository adheres to the Specification-Driven Development directory layout:

```text
learning_management_system/
├── docs/                         # Project documentation, architecture diagrams, reports
├── logs/                         # Audit trails, environment setup records, git-gate logs
│   ├── agent-setup.md            # Agent environment registration
│   ├── git-gate.md               # Gatekeeper decision records & conflict resolutions
│   └── sked-summary.md           # Progress summaries
├── spec/                         # Formal Specifications (Single Source of Truth)
│   ├── concept.md                # System concept baseline
│   ├── srs.md                    # Master Software Requirements Specification
│   └── srs.pdf                   # Compiled formal SRS document
├── src/                          # Production source code
│   ├── backend/                  # FastAPI application package
│   │   ├── app/
│   │   │   ├── core/             # Configuration, logging, database setup
│   │   │   ├── models/           # SQLAlchemy / SQLModel ORM models
│   │   │   ├── schemas/          # Pydantic v2 request/response contracts
│   │   │   ├── services/         # Business logic (Tree, Policy, Wiki, Export)
│   │   │   └── api/              # REST API endpoint routers
│   │   └── main.py               # Application entry point & static SPA mount
│   ├── frontend/                 # React 18 SPA (Vite + Tailwind CSS)
│   └── task_schema.json          # Foundational task contract
├── storage/                      # Managed local storage (created at runtime)
│   ├── db.sqlite3                # SQLite master database (WAL enabled)
│   └── artifacts/                # Sandboxed multi-modal file storage
└── tests/                        # Automated test suites (Mandatory TDD)
    ├── conftest.py               # Pytest fixtures & in-memory SQLite setup
    ├── unit/                     # Fast deterministic unit tests (tree, policies, wiki)
    ├── integration/              # API endpoints, FTS5 queries, and export verification
    └── e2e/                      # Browser workflow validation (Playwright)
```

---

## 🛠️ Development Discipline & Quality Gates

Development strictly follows **Specification-Driven Development (SDD)** and **Test-Driven Development (TDD)**:

$$\text{Requirement ID} \longrightarrow \text{Acceptance Criterion} \longrightarrow \text{Automated Test ID} \longrightarrow \text{Production Module}$$

### Invariants & Gates
1. **Spec as Single Source of Truth**: All behavior must be specified in [`spec/srs.md`](spec/srs.md) prior to implementation.
2. **Red-Green-Refactor**: Unit tests (using in-memory SQLite `:memory:`) must be authored and failing before writing production code.
3. **Mandatory Quality Gates**:
   - Code formatting & linting: `ruff check .` and `ruff format --check .`
   - Strict static typing: `mypy --strict src/`
   - Test suite execution: `pytest tests/unit/ tests/integration/`
   - Test coverage threshold: Minimum **$\ge 90\%$** on all service logic modules.

---

## 🚀 Quickstart & Setup Guide

### Prerequisites
- **Python 3.11+**
- **Node.js 18+** & **npm** (for building the frontend SPA)
- **Git**

### 1. Environment Setup

Clone the repository and initialize the Python virtual environment:

```bash
# Clone the repository
git clone https://github.com/MaksymKorniienko/learning_management_system.git
cd learning_management_system

# Create and activate virtual environment
python -m venv .venv

# On Linux / macOS:
source .venv/bin/activate
# On Windows (PowerShell):
.venv\Scripts\Activate.ps1

# Install backend dependencies
pip install -r requirements.txt
```

### 2. Build Frontend Client

```bash
cd src/frontend
npm install
npm run build
cd ../..
```

The production assets will be generated into `src/frontend/dist/` and served directly by FastAPI.

### 3. Run Application Server

```bash
# Launch server with Uvicorn
uvicorn src.backend.main:app --host 127.0.0.1 --port 8000 --reload
```

Open your browser and navigate to:
- **Web Interface**: `http://localhost:8000`
- **Interactive OpenAPI / Swagger Docs**: `http://localhost:8000/docs`

---

## 🧪 Testing & Verification

Run the test suites with coverage verification:

```bash
# Run isolated fast unit tests
pytest tests/unit/ -v

# Run integration tests (API endpoints & SQLite FTS5)
pytest tests/integration/ -v

# Run all tests with coverage report
pytest --cov=src/backend/app/services --cov-report=term-missing tests/

# Execute type checks and linting
mypy --strict src/
ruff check .
```

---

## 📋 Requirement Identification Scheme

All system functional and non-functional requirements are indexed with formal RFC 2119 assertions:

| Category | Prefix | Scope & Responsibilities |
| :--- | :--- | :--- |
| **Tree Subsystem** | `REQ-TREE-NNN` | Hierarchy depth $\le 5$, strict leaf tasks, deterministic roll-up. |
| **Policy Subsystem** | `REQ-POLICY-NNN` | `READING`, `RESEARCH`, `PRACTICE`, and `PROJECT` completion gates. |
| **Artifact Vault** | `REQ-ARTIFACT-NNN`| Sandboxed filesystem storage, MIME whitelist, guarded rollback. |
| **Knowledge Vault** | `REQ-WIKI-NNN` | `[[wikilinks]]`, atomic refactoring, SQLite FTS5, `#tag` indexing. |
| **Export Engine** | `REQ-EXPORT-NNN` | Mirrored directory layout, relative asset paths, root manifest synthesis. |
| **User Interface** | `REQ-UI-NNN` | Workspace vs. Catalog modes, note editor with scaffolding templates. |
| **Non-Functional** | `REQ-NF-NNN` | $\le 50\text{ms}$ search latency, zero telemetry, CommonMark portability. |

For the complete requirement specifications and BDD acceptance criteria, see [`spec/srs.md`](spec/srs.md).

---

## 🗺️ System Evolution & Roadmap

- [x] **Phase 1: Minimum Viable Product (MVP)**
  - Local-first single-user architecture with zero authentication overhead.
  - Strict tree hierarchy and bottom-up status roll-up algorithm.
  - Multi-modal artifact verification engine and task completion policies.
  - Bidirectional `[[wikilink]]` graph with atomic refactoring and FTS5 search.
  - Dual view paradigms (Workspace Mode vs. Knowledge Catalog Mode).
  - CommonMark tree directory and ZIP export engine.
- [ ] **Phase 2: Post-MVP Roadmap** (See [`spec/srs.md#163`](spec/srs.md#163-phase-2-roadmap-post-mvp-evolution))
  - *Local LLM Compendium Agent*: Opt-in local synthesis summaries (via Ollama / llama-cpp).
  - *Interactive Graph Canvas*: 2D WebGL visualizer for global knowledge connectivity.
  - *Prerequisite DAG Locking*: Sequential task dependency gating.

---

## 📄 License & Academic Attribution

Developed as part of the **Information Systems Design** curriculum:
- **Author / Systems Architect**: Maksym Korniienko (KN-32)
- **Academic Affiliation**: Department of System Design, ESC "IASA", Igor Sikorsky Kyiv Polytechnic Institute
- **Discipline**: Specification-Driven Development (SDD) / Software Engineering
