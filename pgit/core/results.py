from dataclasses import dataclass


@dataclass
class TestResult:
    """Result of a PromptGhost evaluation."""

    id: str
    name: str
    passed: bool

    @property
    def status(self) -> str:
        return "PASS" if self.passed else "FAIL"