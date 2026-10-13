# PromptGhost

> **Git-native behavioral diff for AI applications.**

PromptGhost helps developers detect when changes to an AI prompt cause changes in application behavior.

**Git tells you what changed.**  
**PromptGhost tells you what happened because it changed.**

## Why PromptGhost?

Traditional Git diffs show changes to files, but they don't explain how those changes affect an AI application's behavior.

PromptGhost adds a behavioral testing workflow for AI prompts, allowing developers to define expected behavior, run evaluations, save a baseline, and identify behavioral regressions.

## How It Works

1. **Initialize** — Set up PromptGhost in your project.
2. **Test** — Run behavioral tests against your prompts.
3. **Compare** — Compare current results with the saved baseline.
4. **Review** — Identify behavioral changes before they reach users.

## Features

- **Behavioral regression testing** for AI prompts.
- **Baseline comparisons** to detect changes in model behavior.
- **Readable CLI output** for test results and behavioral differences.
- **YAML-based evaluations** for defining test cases and assertions.
- **Google Gemini integration** for running model evaluations.
- **Git-friendly workflow** designed for existing AI application repositories.
- **Automated tests and CI** using GitHub Actions.

## Requirements

- Python 3.11 or later
- A Google Gemini API key for Gemini-backed evaluations

## Installation

Clone the repository and move into the project directory:

```bash
git clone https://github.com/thenavya/PromptGhost.git
cd PromptGhost
```

Install the project:

```bash
pip install -e .
```

Check that the CLI is available:

```bash
pgit version
```

## Configure Gemini

Set your Gemini API key as an environment variable named `GEMINI_API_KEY`.

On Windows PowerShell:

```powershell
$env:GEMINI_API_KEY="your-api-key"
```

Replace `your-api-key` with your actual key. Keep API keys private and never commit them to Git.

## CLI Commands

| Command | Purpose |
|---|---|
| `pgit version` | Display the installed version |
| `pgit init` | Initialize PromptGhost |
| `pgit test` | Run behavioral evaluations |
| `pgit diff` | Compare results against the saved baseline |
| `pgit commit` | Save the current behavioral baseline |

**Note:** `pgit commit` saves a PromptGhost behavioral baseline; it is not a Git commit.

## Example Evaluation

PromptGhost uses YAML to define behavioral tests. A test can specify a prompt, an input, and assertions for the expected output.

```yaml
tests:
  - id: refund_policy
    prompt: prompts/support.txt
    input: "Can I get a refund?"
    assertions:
      - type: contains
        value: "refund"
```

This example checks whether the model's response contains the word `refund`.

## Example: Detect a Regression

Imagine a prompt change causes a customer-support assistant to stop mentioning a relevant refund policy.

A traditional file diff can show that the prompt changed. PromptGhost can help reveal that the change also affected the model's response.

See the [regression demo](demo/README.md) for an example.

## Project Structure

```text
PromptGhost/
├── .github/
│   └── workflows/
│       └── tests.yml
├── demo/
│   └── README.md
├── prompts/
├── tests/
├── .gitignore
├── LICENSE
└── README.md
```

The project also contains the Python package and configuration files required to run the CLI.

## Testing and Quality

- **66 automated tests passing**
- **95% test coverage** in the reported local test run
- **GitHub Actions** workflow for automated testing on pushes to `main` and pull requests

These figures reflect the reported test run and may change as the project evolves.

## Current Scope and Limitations

PromptGhost is a developer-focused prototype for testing and comparing AI prompt behavior. Results depend on the model, evaluation inputs, assertions, and test configuration.

It does not guarantee that every regression will be detected, and it should not be treated as a substitute for comprehensive testing or production monitoring.

## License

This project is licensed under the [MIT License](LICENSE).
