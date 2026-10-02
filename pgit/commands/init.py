from pathlib import Path


def init_project() -> None:
    """Initialize a new PromptGhost project."""
    root = Path.cwd()

    directories = [
        root / "prompts",
        root / "evals",
        root / ".pgit",
    ]

    for directory in directories:
        directory.mkdir(exist_ok=True)

    config = root / "pgit.yaml"

    if not config.exists():
        config.write_text(
            "version: 1\n"
            "prompts_dir: prompts\n"
            "evals_dir: evals\n",
            encoding="utf-8",
        )

    print("PromptGhost project initialized.")