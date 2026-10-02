from pathlib import Path

import typer

from pgit.core.config import load_config
from pgit.core.engine import run_evaluations
from pgit.core.storage import save_results
from pgit.providers.errors import ProviderError
from pgit.providers.factory import create_provider


def run_evals():
    """Run all PromptGhost evaluations."""

    project_root = Path.cwd()

    try:
        config = load_config(
            project_root / "pgit.yaml"
        )
    except Exception as error:
        print("Failed to load PromptGhost configuration.")
        print(error)
        raise typer.Exit(code=1)

    evals_dir = project_root / config.evals_dir

    try:
        provider = create_provider(
            config.provider
        )
    except (ValueError, ProviderError) as error:
        print("Failed to configure AI provider.")
        print(error)
        raise typer.Exit(code=1)

    try:
        results = run_evaluations(
            evals_dir=evals_dir,
            project_root=project_root,
            provider=provider,
        )
    except ProviderError as error:
        print("AI provider error.")
        print(error)
        raise typer.Exit(code=1)
    except ValueError as error:
        print("Evaluation error.")
        print(error)
        raise typer.Exit(code=1)

    for result in results:
        print(
            f"{result.status}  {result.name}"
        )

    save_results(results)

    if any(
        not result.passed
        for result in results
    ):
        raise typer.Exit(code=1)

    return results