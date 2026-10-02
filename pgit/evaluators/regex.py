import re


def regex(text: str, pattern: str) -> bool:
    """Return True if the response matches the regular expression."""
    return re.search(pattern, text, re.IGNORECASE) is not None