def contains(text: str, expected: str) -> bool:
    """Return True if expected text is found in the response."""
    return expected.lower() in text.lower()