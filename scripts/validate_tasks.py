"""Validate AfriLegalBench task definitions against the task schema."""

import json
import sys
from pathlib import Path


TASK_SCHEMA_PATH = Path("tasks/task_schema.json")


def load_schema(path: Path) -> dict:
    with open(path) as f:
        return json.load(f)


def validate_task(task_path: Path, schema: dict) -> list[str]:
    errors = []

    with open(task_path) as f:
        try:
            task = json.load(f)
        except json.JSONDecodeError as e:
            return [f"Invalid JSON: {e}"]

    required = schema.get("required", [])
    for field in required:
        if field not in task:
            errors.append(f"Missing required field: {field}")

    if "task_name" in task:
        if not isinstance(task["task_name"], str) or not task["task_name"]:
            errors.append("task_name must be a non-empty string")
        else:
            expected_prefix = task_path.stem
            if task["task_name"] != expected_prefix:
                errors.append(
                    f"task_name '{task['task_name']}' does not match filename "
                    f"'{expected_prefix}'"
                )

    if "jurisdiction" in task:
        valid_jurisdictions = schema["properties"]["jurisdiction"]["enum"]
        if task["jurisdiction"] not in valid_jurisdictions:
            errors.append(
                f"jurisdiction must be one of {valid_jurisdictions}, "
                f"got '{task['jurisdiction']}'"
            )

    if "reasoning_type" in task:
        valid_types = schema["properties"]["reasoning_type"]["enum"]
        if task["reasoning_type"] not in valid_types:
            errors.append(
                f"reasoning_type must be one of {valid_types}, "
                f"got '{task['reasoning_type']}'"
            )

    if "dataset" in task:
        if not isinstance(task["dataset"], list) or len(task["dataset"]) == 0:
            errors.append("dataset must be a non-empty array")
        else:
            for i, example in enumerate(task["dataset"]):
                for field in ["id", "input", "target"]:
                    if field not in example:
                        errors.append(f"dataset[{i}] missing required field: {field}")
                    elif not isinstance(example[field], str) or not example[field]:
                        errors.append(f"dataset[{i}].{field} must be a non-empty string")

                if "source" in example and not isinstance(example["source"], str):
                    errors.append(f"dataset[{i}].source must be a string")

    return errors


def main():
    if not TASK_SCHEMA_PATH.exists():
        print(f"Schema file not found: {TASK_SCHEMA_PATH}")
        sys.exit(1)

    schema = load_schema(TASK_SCHEMA_PATH)

    tasks_dir = Path("tasks")
    task_files = sorted(tasks_dir.rglob("*.json"))

    if not task_files:
        print("No task JSON files found.")
        sys.exit(0)

    has_errors = False

    for task_path in task_files:
        if task_path.name == "task_schema.json":
            continue
        if task_path.name == "index.json":
            continue

        errors = validate_task(task_path, schema)
        if errors:
            has_errors = True
            print(f"\n{task_path.relative_to(Path.cwd())}:")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"  PASS  {task_path.name}")

    if has_errors:
        sys.exit(1)

    print(f"\nAll task files validated successfully.")


if __name__ == "__main__":
    main()
