from typer.testing import CliRunner

from pgit.cli import app

runner = CliRunner()


def test_version_command():
    result = runner.invoke(app, ["version"])

    assert result.exit_code == 0
    assert "PromptGhost v0.1.0" in result.output


def test_help_command():
    result = runner.invoke(app, ["--help"])

    assert result.exit_code == 0
    assert "Git-native behavioral diff" in result.output