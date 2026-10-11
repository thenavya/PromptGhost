**# PromptGhost — Regression Demo**



**## What this demonstrates**



**PromptGhost detects behavioral regressions in AI applications when prompts change.**



**## Test scenario**



**We start with a customer-support prompt and two evaluations:**



**- `refund\_policy`: checks whether the response contains `refund`.**

**- `uncertainty`: checks whether the response contains `unsure`.**



**## Results**



**| Scenario | Refund policy | Uncertainty |**

**|---|---|---|**

**| Original prompt | PASS | PASS |**

**| Weakened prompt | UNCHANGED | REGRESSED |**

**| Original prompt restored | UNCHANGED | UNCHANGED |**



**## What this proves**



**A prompt change can preserve one behavior while breaking another. PromptGhost compares the latest evaluation results against a saved behavioral baseline and highlights regressions.**



**## Run the demo**



**From the PromptGhost project directory, run:**



**```powershell**

**pgit test**

**pgit commit**

**```**



**After saving the baseline, change the prompt so it no longer instructs the assistant to admit uncertainty, then run:**



**```powershell**

**pgit test**

**pgit diff**

**```**



**Restore the original prompt and run the tests and diff again.**



**\*\*Note:\*\* Results depend on the configured AI provider and its responses. This demo illustrates regression detection; it does not guarantee that every AI response is correct or safe.**

