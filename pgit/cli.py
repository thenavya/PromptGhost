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
    print("PromptGhost v0.1.0")


@app.command()
def hello():
    """Temporary command used to verify the CLI."""
    print("PromptGhost is working.")


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