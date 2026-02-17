from datetime import datetime

def get_days_from_today(date_str: str) -> int | None:
    """
    Returns the number of days between the given date and today.

    Args:
        date_str (str): A date string in the format 'YYYY-MM-DD'.

    Returns:
        int: Days from the given date to today (negative if in the future).
        None: If the date format is invalid.
    """
    try:
        specified_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return None

    return (datetime.today().date() - specified_date).days