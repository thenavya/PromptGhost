from pathlib import Path

from pydantic import ValidationError

from pgit.core.config import load_evals
from pgit.core.models import EvalFile
from pgit.core.results import TestResult
from pgit.core.runner import run_test
from pgit.providers.base import AIProvider


def run_evaluations(
    evals_dir: Path,
    project_root: Path,
    provider: AIProvider,
) -> list[TestResult]:
    """Run all PromptGhost evaluations."""

    eval_files = sorted(evals_dir.glob("*.yaml"))

    if not eval_files:
        raise ValueError("No evaluation files found.")

    results = []

    for eval_file in eval_files:
        raw_data = load_evals(eval_file)

        try:
            eval_data = EvalFile.model_validate(raw_data)
        except ValidationError as error:
            raise ValueError(
                f"Invalid evaluation file: {eval_file}\n{error}"
            ) from error

        for test in eval_data.tests:
            prompt_path = project_root / test.prompt

            if not prompt_path.exists():
                raise ValueError(
                    f"Prompt file not found: {prompt_path}\n"
                    f"Referenced by evaluation: {eval_file}\n"
                    f"Test: {test.name}"
                )

            prompt = prompt_path.read_text(encoding="utf-8")

            response = provider.generate(
                prompt,
                test.input,
            )

            passed = run_test(
                test.model_dump(),
                response,
            )

            results.append(
                TestResult(
                    id=test.id or test.name,
                    name=test.name,
                    passed=passed,
                )
            )

    return results