from typing import Literal

from pydantic import BaseModel, Field, model_validator


AssertionType = Literal[
    "contains",
    "not_contains",
    "exact_match",
    "regex",
    "json_schema",
]


class AssertionDefinition(BaseModel):
    """A single evaluation assertion."""

    type: AssertionType
    value: str | None = None
    schema: dict | None = None

    @model_validator(mode="after")
    def validate_assertion(self):
        """Validate fields required by each assertion type."""

        if self.type in {
            "contains",
            "not_contains",
            "exact_match",
            "regex",
        }:
            if not self.value:
                raise ValueError(
                    f"Assertion type '{self.type}' requires a 'value'."
                )

        if self.type == "json_schema":
            if not self.schema:
                raise ValueError(
                    "Assertion type 'json_schema' requires a 'schema'."
                )

        return self


class TestDefinition(BaseModel):
    """A single PromptGhost evaluation test."""

    id: str | None = None
    name: str
    prompt: str
    input: str
    assertions: list[AssertionDefinition] = Field(
        default_factory=list
    )


class EvalFile(BaseModel):
    """A PromptGhost evaluation file."""

    tests: list[TestDefinition] = Field(
        default_factory=list
    )