from unittest.mock import patch

from pgit.commands.commit import create_baseline


def test_no_results_prints_message():
    with (
        patch("pgit.commands.commit.load_results", return_value=[]),
        patch("pgit.commands.commit.save_baseline") as save,
        patch("builtins.print") as mock_print,
    ):
        create_baseline()

    mock_print.assert_any_call("No test results found.")
    mock_print.assert_any_call("Run pgit test first.")
    save.assert_not_called()


def test_results_save_baseline():
    results = [object()]

    with (
        patch("pgit.commands.commit.load_results", return_value=results),
        patch("pgit.commands.commit.save_baseline") as save,
        patch("builtins.print") as mock_print,
    ):
        create_baseline()

    save.assert_called_once_with(results)
    mock_print.assert_called_once_with("Behavioral baseline saved.")
