def exact_match(text: str, expected: str) -> bool:
    """Return True if the response exactly matches the expected text."""
    return text.strip().lower() == expected.strip().lower()