import re

def normalize_phone(phone_number: str) -> str:
    """
    Normalizes a phone number to a standard format.
    Adds the Ukrainian country code '+38' if missing.
    """

    # Remove all characters except digits
    normalized = re.sub(r"[^\d]", "", phone_number)

    if normalized.startswith("380"):
        return "+" + normalized

    return "+38" + normalized