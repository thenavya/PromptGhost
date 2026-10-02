from pgit.core.results import TestResult


STATUS_ORDER = {
    "REGRESSED": 0,
    "NEW": 1,
    "REMOVED": 2,
    "IMPROVED": 3,
    "UNCHANGED": 4,
}


def compare_results(
    baseline: list[TestResult],
    current: list[TestResult],
) -> list[tuple[str, str]]:
    """Compare baseline and current test results using stable IDs."""

    baseline_map = {
        result.id: result
        for result in baseline
    }

    current_map = {
        result.id: result
        for result in current
    }

    comparisons = []

    for test_id, current_result in current_map.items():
        baseline_result = baseline_map.get(test_id)

        if baseline_result is None:
            status = "NEW"

        elif baseline_result.passed == current_result.passed:
            status = "UNCHANGED"

        elif baseline_result.passed and not current_result.passed:
            status = "REGRESSED"

        else:
            status = "IMPROVED"

        comparisons.append(
            (current_result.name, status)
        )

    for test_id, baseline_result in baseline_map.items():
        if test_id not in current_map:
            comparisons.append(
                (baseline_result.name, "REMOVED")
            )

    comparisons.sort(
        key=lambda item: (
            STATUS_ORDER[item[1]],
            item[0],
        )
    )

    return comparisons