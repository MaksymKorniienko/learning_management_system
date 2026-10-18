#!/usr/bin/env python3
"""
setup_labels.py: Automated GitHub Labels Provisioning for PKLMS

This script applies the standardized SDD label taxonomy (Statuses, Types, Domains)
to the GitHub repository via the GitHub REST API.

Usage:
    python scripts/setup_labels.py <GITHUB_TOKEN>
    or set environment variable GITHUB_TOKEN
"""

import os
import sys
import json
import urllib.request
import urllib.error

REPO_OWNER = "MaksymKorniienko"
REPO_NAME = "learning_management_system"
API_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/labels"

LABELS = [
    # Statuses
    {"name": "status: todo", "color": "cfd3d7", "description": "Pending task; requirements defined; ready to be picked up for development"},
    {"name": "status: in-progress", "color": "0969da", "description": "Active implementation, test authoring, or drafting is underway by the assignee"},
    {"name": "status: in-review", "color": "d4a72c", "description": "Work completed; awaiting PR review, automated test pass, or quality audit"},
    {"name": "status: blocked", "color": "d93f0b", "description": "Work halted due to an unresolved upstream dependency, defect, or spec ambiguity"},
    {"name": "status: done", "color": "2da44e", "description": "All acceptance criteria satisfied; tests passing; merged to main branch"},
    # SDD Types
    {"name": "type: specification", "color": "1d76db", "description": "Baseline system specification, domain schema, or API contract authored in SRS"},
    {"name": "type: addendum", "color": "5319e7", "description": "Formal amendment, delta, or clarification to an approved baseline specification"},
    {"name": "type: test", "color": "e99695", "description": "Automated unit, integration, or contract test asserting expected failure (TDD Red)"},
    {"name": "type: feature", "color": "006b75", "description": "Production code implementation satisfying passing test contracts (TDD Green)"},
    {"name": "type: verification", "color": "fbca04", "description": "Internal technical quality check: static types, linting, test coverage (>= 90%)"},
    {"name": "type: validation", "color": "bfdadc", "description": "User-centric acceptance: BDD scenarios, user journeys, cognitive invariants"},
    {"name": "type: documentation", "color": "0075ca", "description": "User manuals, API Swagger schemas, README guides, and architecture documentation"},
    {"name": "type: gate", "color": "b60205", "description": "Formal blocking milestone checkpoint verifying prerequisite tickets before merge"},
    # Subsystems
    {"name": "domain: tree", "color": "c2e0c6", "description": "Goal/Module/Task hierarchy, leaf invariants, and status roll-up logic"},
    {"name": "domain: policy", "color": "fef2c0", "description": "Task completion policies (READING, RESEARCH, PRACTICE, PROJECT/LAB)"},
    {"name": "domain: artifact", "color": "bfd4f2", "description": "Artifact vault storage, MIME verification, size bounds, guarded deletion"},
    {"name": "domain: wiki", "color": "d4c5f9", "description": "Bidirectional wikilinks, auto-refactoring, and SQLite FTS5 search"},
    {"name": "domain: export", "color": "f9d0c4", "description": "Portability engine, directory tree mirroring, and README manifest"},
    {"name": "domain: ui", "color": "e6cbf2", "description": "React SPA, Workspace Mode, Knowledge Catalog Mode, and Markdown editor"},
]


def sync_labels(token: str):
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "PKLMS-Label-Sync",
    }

    # Fetch existing labels
    req = urllib.request.Request(f"{API_URL}?per_page=100", headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            existing = {item["name"]: item for item in json.loads(resp.read().decode())}
    except urllib.error.HTTPError as e:
        print(f"Error fetching existing labels: {e.code} - {e.read().decode()}")
        return

    print(f"Found {len(existing)} existing labels in {REPO_OWNER}/{REPO_NAME}.")

    for label in LABELS:
        name = label["name"]
        payload = json.dumps(label).encode("utf-8")

        if name in existing:
            # Update label
            url = f"{API_URL}/{urllib.parse.quote(name)}"
            req = urllib.request.Request(url, data=payload, headers=headers, method="PATCH")
            action = "Updated"
        else:
            # Create label
            req = urllib.request.Request(API_URL, data=payload, headers=headers, method="POST")
            action = "Created"

        try:
            with urllib.request.urlopen(req) as resp:
                print(f"[{action}] '{name}' ({label['color']}) - {label['description']}")
        except urllib.error.HTTPError as e:
            print(f"[Failed] '{name}': {e.code} - {e.read().decode()}")


if __name__ == "__main__":
    import urllib.parse
    token = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("GITHUB_TOKEN")
    if not token:
        print("Usage: python scripts/setup_labels.py <GITHUB_TOKEN>")
        print("Or set GITHUB_TOKEN environment variable.")
        sys.exit(1)
    sync_labels(token)
