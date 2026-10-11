from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
from pydantic import ValidationError

from pgit.core.engine import run_evaluations


def test_no_evaluation_files_found(tmp_path):
    with pytest.raises(ValueError, match="No evaluation files found"):
        run_evaluations(tmp_path, tmp_path, MagicMock())


def test_missing_prompt_file(tmp_path):
    evals_dir = tmp_path / "evals"
    evals_dir.mkdir()

    eval_file = evals_dir / "test.yaml"
    eval_file.write_text("placeholder", encoding="utf-8")

    eval_data = MagicMock()
    eval_data.tests = [
        MagicMock(
            prompt="missing.txt",
            name="Missing prompt",
        )
    ]

    with (
        patch("pgit.core.engine.load_evals", return_value={}),
        patch(
            "pgit.core.engine.EvalFile.model_validate",
            return_value=eval_data,
        ),
    ):
        with pytest.raises(ValueError, match="Prompt file not found"):
            run_evaluations(evals_dir, tmp_path, MagicMock())


def test_invalid_evaluation_data_raises_value_error(tmp_path):
    evals_dir = tmp_path / "evals"
    evals_dir.mkdir()
    (evals_dir / "test.yaml").write_text("placeholder", encoding="utf-8")

    with (
        patch("pgit.core.engine.load_evals", return_value={}),
        patch(
            "pgit.core.engine.EvalFile.model_validate",
            side_effect=ValidationError.from_exception_data(
                "EvalFile",
                [],
            ),
        ),
    ):
        with pytest.raises(ValueError, match="Invalid evaluation file"):
            run_evaluations(evals_dir, tmp_path, MagicMock())
def test_successful_evaluation(tmp_path):
    evals_dir = tmp_path / "evals"
    evals_dir.mkdir()

    prompt_file = tmp_path / "prompt.txt"
    prompt_file.write_text("Be helpful.", encoding="utf-8")

    eval_file = evals_dir / "test.yaml"
    eval_file.write_text("placeholder", encoding="utf-8")

    test_case = MagicMock()
    test_case.prompt = "prompt.txt"
    test_case.input = "Hello"
    test_case.name = "Greeting"
    test_case.id = "greeting-1"
    test_case.model_dump.return_value = {"name": "Greeting"}

    eval_data = MagicMock()
    eval_data.tests = [test_case]

    provider = MagicMock()
    provider.generate.return_value = "Hello there!"

    with (
        patch("pgit.core.engine.load_evals", return_value={}),
        patch(
            "pgit.core.engine.EvalFile.model_validate",
            return_value=eval_data,
        ),
        patch("pgit.core.engine.run_test", return_value=True),
    ):
        results = run_evaluations(evals_dir, tmp_path, provider)

    assert len(results) == 1
    assert results[0].passed is True
    assert results[0].name == "Greeting"
    provider.generate.assert_called_once_with("Be helpful.", "Hello")
def test_failed_evaluation_returns_failed_result(tmp_path):
    evals_dir = tmp_path / "evals"
    evals_dir.mkdir()

    prompt_file = tmp_path / "prompt.txt"
    prompt_file.write_text("Be helpful.", encoding="utf-8")

    eval_file = evals_dir / "test.yaml"
    eval_file.write_text("placeholder", encoding="utf-8")

    test_case = MagicMock()
    test_case.prompt = "prompt.txt"
    test_case.input = "Hello"
    test_case.name = "Greeting"
    test_case.id = "greeting-1"
    test_case.model_dump.return_value = {"name": "Greeting"}

    eval_data = MagicMock()
    eval_data.tests = [test_case]

    provider = MagicMock()
    provider.generate.return_value = "Unexpected response"

    with (
        patch("pgit.core.engine.load_evals", return_value={}),
        patch(
            "pgit.core.engine.EvalFile.model_validate",
            return_value=eval_data,
        ),
        patch("pgit.core.engine.run_test", return_value=False),
    ):
        results = run_evaluations(evals_dir, tmp_path, provider)

    assert len(results) == 1
    assert results[0].passed is False
    assert results[0].name == "Greeting"
