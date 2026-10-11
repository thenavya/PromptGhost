import typer

from pgit.commands.commit import create_baseline
from pgit.commands.diff import run_diff
from pgit.commands.init import init_project
from pgit.commands.test import run_evals

app = typer.Typer(
    name="pgit",
    help="Git-native behavioral diff for AI applications.",
)


@app.command()
def version():
    """Show the PromptGhost version."""
    from importlib.metadata import version as get_version, PackageNotFoundError

    try:
        package_version = get_version("promptghost")
    except PackageNotFoundError:
        package_version = "0.1.0"

    print(f"PromptGhost v{package_version}")



@app.command(name="init")
def init():
    """Initialize a PromptGhost project."""
    init_project()


@app.command(name="test")
def test():
    """Run PromptGhost evaluations."""
    run_evals()


@app.command(name="diff")
def diff():
    """Show behavioral differences between results."""
    run_diff()


@app.command(name="commit")
def commit():
    """Save current test results as the behavioral baseline."""
    create_baseline()


if __name__ == "__main__":
    app()