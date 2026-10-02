import json

from pydantic import BaseModel, ValidationError


def json_schema(text: str, schema: dict) -> bool:
    """Return True if the response is valid JSON matching the schema."""
    try:
        data = json.loads(text)
        model = create_model_from_schema(schema)
        model.model_validate(data)
        return True
    except (json.JSONDecodeError, ValidationError, TypeError):
        return False


def create_model_from_schema(schema: dict) -> type[BaseModel]:
    """Create a Pydantic model from a simple JSON schema."""
    from pydantic import create_model

    fields = {}

    for name, field in schema.get("properties", {}).items():
        field_type = str

        if field.get("type") == "integer":
            field_type = int
        elif field.get("type") == "number":
            field_type = float
        elif field.get("type") == "boolean":
            field_type = bool

        if name in schema.get("required", []):
            fields[name] = (field_type, ...)
        else:
            fields[name] = (field_type, None)

    return create_model("PromptGhostSchema", **fields)