from pgit.core.storage import load_results, save_baseline


def create_baseline() -> None:
    """Save current test results as the behavioral baseline."""
    results = load_results()

    if not results:
        print("No test results found.")
        print("Run pgit test first.")
        return

    save_baseline(results)

    print("Behavioral baseline saved.")