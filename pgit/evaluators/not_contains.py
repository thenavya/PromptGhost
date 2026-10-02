def not_contains(text: str, unexpected: str) -> bool:
    """Return True if unexpected text is not found in the response."""
    return unexpected.lower() not in text.lower()