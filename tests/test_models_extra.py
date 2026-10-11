
import pytest
from pydantic import ValidationError

from pgit.core.models import (
    AssertionDefinition,
    EvalFile,
    TestDefinition as PromptTestDefinition,
)


@pytest.mark.parametrize(
    "assertion_type",
    ["contains", "not_contains", "exact_match", "regex"],
)
def test_assertion_types_require_value(assertion_type):
    with pytest.raises(ValidationError, match="requires a 'value'"):
        AssertionDefinition(type=assertion_type)


def test_assertion_rejects_empty_value():
    with pytest.raises(ValidationError, match="requires a 'value'"):
        AssertionDefinition(type="contains", value="")


def test_json_schema_assertion_requires_schema():
    with pytest.raises(ValidationError, match="requires a 'schema'"):
        AssertionDefinition(type="json_schema")


def test_json_schema_assertion_accepts_schema_alias():
    assertion = AssertionDefinition(
        type="json_schema",
        **{"schema": {"type": "object"}},
    )

    assert assertion.json_schema == {"type": "object"}


def test_assertion_rejects_unknown_type():
    with pytest.raises(ValidationError):
        AssertionDefinition(type="unknown", value="example")


def test_test_definition_defaults():
    test = PromptTestDefinition(
        name="Greeting",
        prompt="greeting.txt",
        input="Hello",
    )

    assert test.id is None
    assert test.assertions == []


def test_eval_file_defaults_to_empty_tests():
    eval_file = EvalFile()

    assert eval_file.tests == []


def test_eval_file_parses_nested_assertions():
    eval_file = EvalFile(
        tests=[
            {
                "name": "Greeting",
                "prompt": "greeting.txt",
                "input": "Hello",
                "assertions": [
                    {"type": "contains", "value": "Hello"}
                ],
            }
        ]
    )

    assert len(eval_file.tests) == 1
    assert eval_file.tests[0].assertions[0].type == "contains"
