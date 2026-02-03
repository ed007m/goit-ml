from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list[dict[str, str]]) -> list[dict[str, str]]:
    """
    Returns users with birthdays in the next 7 days (including today).
    If a birthday falls on a weekend, the congratulation date moves to Monday.

    Args:
        users (list): List of dicts with 'name' (str) and 'birthday' ('YYYY.MM.DD').

    Returns:
        list: List of dicts with 'name' and 'congratulation_date' ('YYYY.MM.DD').
    """

    today = datetime.today().date()

    upcoming = []
    for user in users:
        bd = datetime.strptime(user['birthday'], "%Y.%m.%d").date()
        bd_this_year = bd.replace(year=today.year)
        if bd_this_year < today:
            bd_this_year = bd_this_year.replace(year=today.year + 1)

        days_until = (bd_this_year - today).days
        if 0 <= days_until <= 7:
            if bd_this_year.weekday() == 5:  # Saturday
                bd_this_year += timedelta(days=2)
            elif bd_this_year.weekday() == 6:  # Sunday
                bd_this_year += timedelta(days=1)

            upcoming.append({
                "name": user["name"],
                "congratulation_date": bd_this_year.strftime("%Y.%m.%d")
            })

    return upcoming
