
from pathlib import Path

import pytest
from pydantic import ValidationError

from pgit.core.config import load_config, load_evals


def test_load_config_uses_defaults_when_file_is_empty(tmp_path):
    config_file = tmp_path / "pgit.yaml"
    config_file.write_text("", encoding="utf-8")

    config = load_config(config_file)

    assert config.version == 1
    assert config.prompts_dir == "prompts"
    assert config.evals_dir == "evals"
    assert config.provider == "mock"


def test_load_config_reads_custom_values(tmp_path):
    config_file = tmp_path / "pgit.yaml"
    config_file.write_text(
        "version: 2\n"
        "prompts_dir: custom_prompts\n"
        "evals_dir: custom_evals\n"
        "provider: gemini\n",
        encoding="utf-8",
    )

    config = load_config(config_file)

    assert config.version == 2
    assert config.prompts_dir == "custom_prompts"
    assert config.evals_dir == "custom_evals"
    assert config.provider == "gemini"


def test_load_config_rejects_invalid_provider(tmp_path):
    config_file = tmp_path / "pgit.yaml"
    config_file.write_text("provider: unknown\n", encoding="utf-8")

    with pytest.raises(ValidationError):
        load_config(config_file)


def test_load_evals_returns_empty_dict_for_empty_file(tmp_path):
    eval_file = tmp_path / "evals.yaml"
    eval_file.write_text("", encoding="utf-8")

    assert load_evals(eval_file) == {}


def test_load_evals_reads_yaml_data(tmp_path):
    eval_file = tmp_path / "evals.yaml"
    eval_file.write_text(
        "tests:\n"
        "  - name: greeting\n"
        "    prompt: greeting.txt\n",
        encoding="utf-8",
    )

    data = load_evals(eval_file)

    assert data["tests"][0]["name"] == "greeting"
    assert data["tests"][0]["prompt"] == "greeting.txt"


def test_load_config_missing_file_raises_error(tmp_path):
    missing_file = tmp_path / "missing.yaml"

    with pytest.raises(FileNotFoundError):
        load_config(missing_file)
