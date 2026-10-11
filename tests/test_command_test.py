
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import pytest
import typer

from pgit.commands.test import run_evals
from pgit.providers.errors import ProviderRequestError


def test_successful_evaluations(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    config = SimpleNamespace(evals_dir="evals", provider="mock")
    results = [SimpleNamespace(status="PASS", name="Refund policy", passed=True)]

    with (
        patch("pgit.commands.test.load_config", return_value=config),
        patch("pgit.commands.test.create_provider", return_value=object()),
        patch("pgit.commands.test.run_evaluations", return_value=results),
        patch("pgit.commands.test.save_results") as save_results,
    ):
        returned = run_evals()

    assert returned == results
    save_results.assert_called_once_with(results)


def test_configuration_failure_exits(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    with patch(
        "pgit.commands.test.load_config",
        side_effect=ValueError("invalid config"),
    ):
        with pytest.raises(typer.Exit) as exc:
            run_evals()

    assert exc.value.exit_code == 1


def test_provider_configuration_failure_exits(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    config = SimpleNamespace(evals_dir="evals", provider="unknown")

    with (
        patch("pgit.commands.test.load_config", return_value=config),
        patch(
            "pgit.commands.test.create_provider",
            side_effect=ValueError("unknown provider"),
        ),
    ):
        with pytest.raises(typer.Exit) as exc:
            run_evals()

    assert exc.value.exit_code == 1


def test_provider_request_failure_exits(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    config = SimpleNamespace(evals_dir="evals", provider="mock")

    with (
        patch("pgit.commands.test.load_config", return_value=config),
        patch("pgit.commands.test.create_provider", return_value=object()),
        patch(
            "pgit.commands.test.run_evaluations",
            side_effect=ProviderRequestError("request failed"),
        ),
    ):
        with pytest.raises(typer.Exit) as exc:
            run_evals()

    assert exc.value.exit_code == 1


def test_failed_evaluation_exits_with_code_one(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    config = SimpleNamespace(evals_dir="evals", provider="mock")
    results = [SimpleNamespace(status="FAIL", name="Refund policy", passed=False)]

    with (
        patch("pgit.commands.test.load_config", return_value=config),
        patch("pgit.commands.test.create_provider", return_value=object()),
        patch("pgit.commands.test.run_evaluations", return_value=results),
        patch("pgit.commands.test.save_results"),
    ):
        with pytest.raises(typer.Exit) as exc:
            run_evals()

    assert exc.value.exit_code == 1
