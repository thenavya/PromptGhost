import typer

from pgit.core.comparator import compare_results
from pgit.core.storage import load_baseline, load_results


def run_diff() -> None:
    """Compare current results with the behavioral baseline."""
    baseline = load_baseline()
    current = load_results()

    if not baseline:
        print("No baseline found.")
        print("Run a baseline commit first.")
        raise typer.Exit(code=1)

    comparisons = compare_results(baseline, current)

    has_regression = False

    for name, status in comparisons:
        print(f"{status:<12} {name}")

        if status in {"REGRESSED", "REMOVED"}:
            has_regression = True

    if has_regression:
        raise typer.Exit(code=1)