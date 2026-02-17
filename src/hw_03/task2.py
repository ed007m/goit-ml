import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    """
    Returns a sorted list of unique random integers within the given range.
    Returns an empty list if the input parameters are invalid.
    """
    if (
        min < 1 or
        max > 1000 or
        min > max or
        quantity < 1 or
        quantity > (max - min + 1)
    ):
        return []

    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)