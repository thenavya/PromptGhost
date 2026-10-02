import json
from pathlib import Path

from pgit.core.results import TestResult


RESULTS_FILE = Path(".pgit/results.json")
BASELINE_FILE = Path(".pgit/baseline.json")


def save_results(results: list[TestResult]) -> None:
    """Save current test results."""
    RESULTS_FILE.parent.mkdir(exist_ok=True)

    data = [
        {
            "id": result.id,
            "name": result.name,
            "passed": result.passed,
        }
        for result in results
    ]

    RESULTS_FILE.write_text(
        json.dumps(data, indent=2),
        encoding="utf-8",
    )


def load_results() -> list[TestResult]:
    """Load current test results."""
    return _load_file(RESULTS_FILE)


def save_baseline(results: list[TestResult]) -> None:
    """Save test results as the behavioral baseline."""
    BASELINE_FILE.parent.mkdir(exist_ok=True)

    data = [
        {
            "id": result.id,
            "name": result.name,
            "passed": result.passed,
        }
        for result in results
    ]

    BASELINE_FILE.write_text(
        json.dumps(data, indent=2),
        encoding="utf-8",
    )


def load_baseline() -> list[TestResult]:
    """Load the behavioral baseline."""
    return _load_file(BASELINE_FILE)


def _load_file(path: Path) -> list[TestResult]:
    """Load TestResult objects from a JSON file."""
    if not path.exists():
        return []

    data = json.loads(
        path.read_text(encoding="utf-8")
    )

    return [
        TestResult(
            id=item.get("id", item["name"]),
            name=item["name"],
            passed=item["passed"],
        )
        for item in data
    ]