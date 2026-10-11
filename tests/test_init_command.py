
from pathlib import Path
from unittest.mock import patch

from pgit.commands.init import init_project


def test_init_creates_project_directories_and_config(tmp_path):
    with patch("pgit.commands.init.Path.cwd", return_value=tmp_path):
        with patch("builtins.print") as mock_print:
            init_project()

    assert (tmp_path / "prompts").is_dir()
    assert (tmp_path / "evals").is_dir()
    assert (tmp_path / ".pgit").is_dir()

    config = tmp_path / "pgit.yaml"
    assert config.exists()
    assert config.read_text(encoding="utf-8") == (
        "version: 1\n"
        "prompts_dir: prompts\n"
        "evals_dir: evals\n"
    )
    mock_print.assert_called_once_with(
        "PromptGhost project initialized."
    )


def test_init_preserves_existing_config(tmp_path):
    config = tmp_path / "pgit.yaml"
    config.write_text("existing: true\n", encoding="utf-8")

    with patch("pgit.commands.init.Path.cwd", return_value=tmp_path):
        init_project()

    assert config.read_text(encoding="utf-8") == "existing: true\n"


def test_init_works_when_directories_already_exist(tmp_path):
    (tmp_path / "prompts").mkdir()
    (tmp_path / "evals").mkdir()
    (tmp_path / ".pgit").mkdir()

    with patch("pgit.commands.init.Path.cwd", return_value=tmp_path):
        init_project()

    assert (tmp_path / "prompts").is_dir()
    assert (tmp_path / "evals").is_dir()
    assert (tmp_path / ".pgit").is_dir()
