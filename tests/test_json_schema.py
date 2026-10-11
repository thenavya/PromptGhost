
from pgit.evaluators.json_schema import json_schema, create_model_from_schema


def test_valid_json_matches_schema():
    schema = {
        "properties": {"name": {"type": "string"}},
        "required": ["name"],
    }
    assert json_schema('{"name": "Navya"}', schema) is True


def test_invalid_json_returns_false():
    schema = {"properties": {"name": {"type": "string"}}}
    assert json_schema('{"name": ', schema) is False


def test_missing_required_field_returns_false():
    schema = {
        "properties": {"name": {"type": "string"}},
        "required": ["name"],
    }
    assert json_schema("{}", schema) is False


def test_wrong_field_type_returns_false():
    schema = {
        "properties": {"age": {"type": "integer"}},
        "required": ["age"],
    }
    assert json_schema('{"age": "twenty"}', schema) is False


def test_optional_field_can_be_omitted():
    schema = {"properties": {"name": {"type": "string"}}}
    assert json_schema("{}", schema) is True


def test_create_model_from_schema():
    schema = {
        "properties": {"active": {"type": "boolean"}},
        "required": ["active"],
    }
    model = create_model_from_schema(schema)
    assert model.model_validate({"active": True}).active is True
