from unittest.mock import patch

import pytest
import typer

from pgit.commands.diff import run_diff


def test_missing_baseline_exits():
    with (
        patch("pgit.commands.diff.load_baseline", return_value=[]),
        patch("pgit.commands.diff.load_results", return_value=[]),
        patch("builtins.print") as mock_print,
    ):
        with pytest.raises(typer.Exit) as exc:
            run_diff()

    assert exc.value.exit_code == 1
    mock_print.assert_any_call("No baseline found.")
    mock_print.assert_any_call("Run a baseline commit first.")


def test_normal_comparison_does_not_exit():
    baseline = [object()]
    current = [object()]

    with (
        patch("pgit.commands.diff.load_baseline", return_value=baseline),
        patch("pgit.commands.diff.load_results", return_value=current),
        patch(
            "pgit.commands.diff.compare_results",
            return_value=[("Greeting", "UNCHANGED")],
        ),
        patch("builtins.print") as mock_print,
    ):
        run_diff()

    mock_print.assert_called_once_with(f"{'UNCHANGED':<12} Greeting")


@pytest.mark.parametrize("status", ["REGRESSED", "REMOVED"])
def test_regression_or_removal_exits(status):
    with (
        patch("pgit.commands.diff.load_baseline", return_value=[object()]),
        patch("pgit.commands.diff.load_results", return_value=[object()]),
        patch(
            "pgit.commands.diff.compare_results",
            return_value=[("Greeting", status)],
        ),
    ):
        with pytest.raises(typer.Exit) as exc:
            run_diff()

    assert exc.value.exit_code == 1
