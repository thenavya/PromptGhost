from pgit.evaluators.contains import contains
from pgit.evaluators.exact_match import exact_match
from pgit.evaluators.json_schema import json_schema
from pgit.evaluators.not_contains import not_contains
from pgit.evaluators.regex import regex


def evaluate(response: str, assertion: dict) -> bool:
    """Evaluate a single assertion against an AI response."""
    assertion_type = assertion.get("type")

    if assertion_type == "contains":
        return contains(response, assertion["value"])

    if assertion_type == "not_contains":
        return not_contains(response, assertion["value"])

    if assertion_type == "exact_match":
        return exact_match(response, assertion["value"])

    if assertion_type == "regex":
        return regex(response, assertion["value"])

    if assertion_type == "json_schema":
        return json_schema(response, assertion["schema"])

    raise ValueError(f"Unknown assertion type: {assertion_type}")