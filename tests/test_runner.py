
import pytest

from pgit.evaluators.runner import evaluate


def test_contains_assertion():
    assert evaluate("Hello world", {"type": "contains", "value": "world"}) is True


def test_not_contains_assertion():
    assert evaluate("Hello world", {"type": "not_contains", "value": "goodbye"}) is True


def test_exact_match_assertion():
    assert evaluate("Hello", {"type": "exact_match", "value": "Hello"}) is True


def test_regex_assertion():
    assert evaluate("Order 123", {"type": "regex", "value": r"\d+"}) is True


def test_json_schema_assertion():
    assertion = {
        "type": "json_schema",
        "schema": {
            "properties": {"name": {"type": "string"}},
            "required": ["name"],
        },
    }
    assert evaluate('{"name": "Navya"}', assertion) is True


def test_unknown_assertion_type_raises_error():
    with pytest.raises(ValueError, match="Unknown assertion type"):
        evaluate("Hello", {"type": "unknown"})
