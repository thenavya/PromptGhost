from pgit.evaluators.runner import evaluate


def run_test(test: dict, response: str) -> bool:
    """Run all assertions for one test."""
    assertions = test.get("assertions", [])

    return all(
        evaluate(response, assertion)
        for assertion in assertions
    )