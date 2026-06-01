"""Annotation pipeline helper for AfriLegalBench.

Usage:
    python scripts/annotate.py review <task_file>       # Review a single task
    python scripts/annotate.py review_all <jurisdiction> # Review all tasks in a jurisdiction
    python scripts/annotate.py validate <task_file>      # Check format and completeness
"""

import json
import sys
from pathlib import Path


TASKS_DIR = Path("tasks")


def load_task(path: Path) -> dict:
    with open(path) as f:
        return json.load(f)


def review_task(task: dict, path: Path):
    """Print a human-readable review of a task."""
    print(f"{'='*60}")
    print(f"Task: {task.get('task_name', 'UNNAMED')}")
    print(f"File: {path.relative_to(Path.cwd())}")
    print(f"{'='*60}")
    print(f"Jurisdiction: {task.get('jurisdiction', 'N/A')}")
    print(f"Legal system: {', '.join(task.get('legal_system', []))}")
    print(f"Reasoning type: {task.get('reasoning_type', 'N/A')}")
    print(f"Languages: {', '.join(task.get('languages', []))}")
    print(f"\nExamples ({len(task.get('dataset', []))} total):")
    print("-" * 60)

    for i, example in enumerate(task.get("dataset", [])):
        print(f"\n  [{i+1}] ID: {example.get('id', 'N/A')}")
        print(f"      Input:   {example.get('input', '')[:200]}")
        print(f"      Target:  {example.get('target', '')[:200]}")
        if example.get("source"):
            print(f"      Source:  {example.get('source', '')[:100]}")
        print()

    print(f"{'='*60}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    command = sys.argv[1]

    if command == "review":
        if len(sys.argv) < 3:
            print("Usage: python scripts/annotate.py review <task_file>")
            sys.exit(1)
        task_path = Path(sys.argv[2])
        if not task_path.exists():
            print(f"File not found: {task_path}")
            sys.exit(1)
        task = load_task(task_path)
        review_task(task, task_path)

    elif command == "review_all":
        jurisdiction = sys.argv[2] if len(sys.argv) > 2 else None
        if jurisdiction:
            pattern = f"tasks/{jurisdiction}/**/*.json"
            paths = sorted(TASKS_DIR.rglob(f"{jurisdiction}/**/*.json"))
        else:
            paths = sorted(TASKS_DIR.rglob("*.json"))

        for task_path in paths:
            if task_path.name in ("task_schema.json", "index.json"):
                continue
            task = load_task(task_path)
            review_task(task, task_path)
            input("Press Enter to continue to the next task...")

    elif command == "validate":
        from validate_tasks import load_schema, validate_task

        if len(sys.argv) < 3:
            print("Usage: python scripts/annotate.py validate <task_file>")
            sys.exit(1)

        task_path = Path(sys.argv[2])
        if not task_path.exists():
            print(f"File not found: {task_path}")
            sys.exit(1)

        schema_path = TASKS_DIR / "task_schema.json"
        if not schema_path.exists():
            print(f"Schema file not found: {schema_path}")
            sys.exit(1)

        schema = load_schema(schema_path)
        errors = validate_task(task_path, schema)

        if errors:
            print(f"\nValidation errors for {task_path.name}:")
            for err in errors:
                print(f"  - {err}")
            sys.exit(1)
        else:
            print(f"  PASS  {task_path.name}")

    else:
        print(f"Unknown command: {command}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
