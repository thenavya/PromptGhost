from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel


ProviderName = Literal[
    "mock",
    "gemini",
]


class PromptGhostConfig(BaseModel):
    """PromptGhost project configuration."""

    version: int = 1
    prompts_dir: str = "prompts"
    evals_dir: str = "evals"
    provider: ProviderName = "mock"


def load_config(
    path: Path = Path("pgit.yaml"),
) -> PromptGhostConfig:
    """Load and validate PromptGhost configuration."""

    with path.open(
        "r",
        encoding="utf-8",
    ) as file:
        data = yaml.safe_load(file) or {}

    return PromptGhostConfig.model_validate(data)


def load_evals(path: Path) -> dict:
    """Load evaluation definitions from a YAML file."""

    with path.open(
        "r",
        encoding="utf-8",
    ) as file:
        return yaml.safe_load(file) or {}