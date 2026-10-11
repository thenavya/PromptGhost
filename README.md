**# PromptGhost**



**> Git-native behavioral diff for AI applications.**



**PromptGhost helps developers detect when changes to an AI prompt cause changes in application behavior.**



**Git tells you \*\*what changed\*\*.**  

**PromptGhost tells you \*\*what happened because it changed\*\*.**



**## The Problem**



**Changing an AI prompt can silently change your application's behavior.**



**A normal Git diff can show:**



**```diff**

**- Answer the customer's question.**

**+ Answer the customer's question concisely.**

**```**



**But it cannot tell you whether the new prompt caused the AI to break a refund policy, ignore a safety instruction, or produce an unexpected answer.**



**PromptGhost adds behavior-level testing and regression detection to AI applications.**



**## How It Works**



**1. Write evaluation cases for your AI prompt.**

**2. Run the tests against your configured AI provider.**

**3. Save a passing behavioral baseline.**

**4. Change your prompt and run the tests again.**

**5. Compare the results to detect regressions.**



**## Current Features**



**- \*\*AI provider integration:\*\* Run evaluations using Google Gemini.**

**- \*\*YAML-based evaluations:\*\* Define test cases outside your application code.**

**- \*\*Behavioral assertions:\*\* Check for required text, forbidden text, exact matches, regular expressions, and JSON schema validity.**

**- \*\*Test results:\*\* See which evaluation cases pass or fail.**

**- \*\*Behavioral baselines:\*\* Save a reference set of evaluation results.**

**- \*\*Regression detection:\*\* Identify regressed, improved, unchanged, new, and removed test cases.**

**- \*\*CLI workflow:\*\* Run tests and compare behavior from the terminal.**



**## Quick Start**



**### Requirements**



**- Python 3.10 or later**

**- A Google Gemini API key for Gemini-backed evaluations**



**### Installation**



**Clone the repository:**



**```bash**

**git clone https://github.com/thenavya/PromptGhost.git**

**cd PromptGhost**

**```**



**Create and activate a virtual environment on Windows PowerShell:**



**```powershell**

**python -m venv .venv**

**.\\.venv\\Scripts\\Activate.ps1**

**```**



**Install the project:**



**```powershell**

**pip install -e .**

**```**



**Set your Gemini API key in PowerShell for the current session:**



**```powershell**

**$env:GEMINI\_API\_KEY = "YOUR\_GEMINI\_API\_KEY"**

**```**



**Replace the placeholder with your own API key. Never commit API keys to GitHub.**



**## Basic Workflow**



**Run the evaluation tests:**



**```bash**

**pgit test**

**```**



**Save the current results as the behavioral baseline:**



**```bash**

**pgit commit**

**```**



**Compare the latest results with the saved baseline:**



**```bash**

**pgit diff**

**```**



**\*\*Note:\*\* `pgit commit` saves a PromptGhost behavioral baseline; it does not create a Git commit.**



**## Example: Detecting a Regression**



**Suppose your original support prompt passes two tests:**



**```text**

**PASS  refund\_policy**

**PASS  uncertainty**

**```**



**You change the prompt in a way that causes the refund-policy test to fail.**



**PromptGhost can report:**



**```text**

**FAIL  refund\_policy**

**PASS  uncertainty**

**```**



**After comparing against the saved baseline, the behavioral diff identifies the regression:**



**```text**

**REGRESSED  refund\_policy**

**UNCHANGED  uncertainty**

**```**



**This makes prompt-related behavior changes easier to detect before they reach users.**



**## Evaluation Format**



**Evaluation cases are defined in YAML.**



**Example:**



**```yaml**

**tests:**

&#x20; **- id: refund\_policy**

&#x20;   **prompt: prompts/support.txt**

&#x20;   **input: "Can I get a refund?"**

&#x20;   **assertions:**

&#x20;     **- type: contains**

&#x20;       **value: "refund"**

**```**



**The available assertion types include:**



**- `contains`**

**- `not\_contains`**

**- `exact\_match`**

**- `regex`**

**- `json\_schema`**



**Refer to the repository's `evals/` directory for the project's actual evaluation configuration and examples.**



**## CLI Commands**



**| Command | Purpose |**

**|---|---|**

**| `pgit init` | Initialize PromptGhost configuration |**

**| `pgit test` | Run configured behavioral evaluations |**

**| `pgit commit` | Save the current behavioral baseline |**

**| `pgit diff` | Compare current results with the baseline |**



**## Project Architecture**



**```text**

**PromptGhost/**

**├── pgit/**

**│   ├── commands/**

**│   ├── core/**

**│   ├── evaluators/**

**│   └── providers/**

**├── evals/**

**├── prompts/**

**├── .pgit/**

**├── pgit.yaml**

**├── pyproject.toml**

**└── README.md**

**```**



**- `commands/` contains the CLI commands.**

**- `core/` handles configuration, execution, results, storage, and comparison.**

**- `evaluators/` implements behavioral assertions.**

**- `providers/` integrates AI providers.**

**- `evals/` contains evaluation cases.**

**- `prompts/` contains prompt files.**

**- `.pgit/` stores local behavioral results and baselines.**



**## Why PromptGhost?**



**Traditional version control tracks source-code changes. AI applications also need a way to understand how those changes affect model behavior.**



**PromptGhost explores a practical workflow for testing, recording, and comparing that behavior alongside normal development.**



**## Project Status**

## Project Status

PromptGhost is an actively developed developer tool for behavioral testing and regression detection in AI applications.

The project currently includes YAML-based evaluations, configurable assertion types, a Google Gemini provider, behavioral baselines, and CLI-based regression comparisons.

**Current testing status:** 66 tests passing and 95% reported code coverage.

PromptGhost is an experimental project intended to help developers identify unintended behavior changes during prompt development. It does not guarantee the correctness, safety, or consistency of model outputs.

**PromptGhost is an actively developed project. Its**

