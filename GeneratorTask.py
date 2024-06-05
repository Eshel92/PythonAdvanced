def gen_secs():
    """
    Generate all possible seconds in a minute (0-59).

    Yields:
        int: The next second.
    """
    return (sec for sec in range(60))


def gen_minutes():
    """
    Generate all possible minutes in an hour (0-59).

    Yields:
        int: The next minute.
    """
    return (min for min in range(60))


def gen_hours():
    """
    Generate all possible hours in a day (0-23).

    Yields:
        int: The next hour.
    """
    return (hour for hour in range(24))


def gen_time():
    """
    Generate all possible times in a day in the format hh:mm:ss.

    Yields:
        str: The next time in hh:mm:ss format.
    """
    for hour in gen_hours():
        for minute in gen_minutes():
            for second in gen_secs():
                yield f"{hour:02d}:{minute:02d}:{second:02d}"


def gen_years(start=2024):
    """
    Generate an infinite sequence of years starting from the given year.

    Args:
        start (int): The year to start from. Default is 2024.

    Yields:
        int: The next year.
    """
    while True:
        yield start
        start += 1


def gen_months():
    """
    Generate all possible months in a year (1-12).

    Yields:
        int: The next month.
    """
    for month in range(1, 13):
        yield month


def gen_days(month, leap_year=True):
    """
    Generate all possible days in a given month, considering leap years.

    Args:
        month (int): The month (1-12).
        leap_year (bool): Whether the year is a leap year. Default is True.

    Yields:
        int: The next day in the month.
    """
    if month == 2:
        if leap_year:
            yield from range(1, 30)
        else:
            yield from range(1, 29)
    elif month in [4, 6, 9, 11]:
        yield from range(1, 31)
    else:
        yield from range(1, 32)


def gen_date():
    """
    Generate all possible dates starting from the current year in the format dd/mm/yyyy hh:mm:ss.

    Yields:
        str: The next date in dd/mm/yyyy hh:mm:ss format.
    """
    for year in gen_years():
        for month in gen_months():
            leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
            for day in gen_days(month, leap_year):
                for hour in gen_hours():
                    for minute in gen_minutes():
                        for second in gen_secs():
                            yield f"{day:02d}/{month:02d}/{year} {hour:02d}:{minute:02d}:{second:02d}"


gen = gen_date()
i = 0
while True:
    i += 1
    date = next(gen)
    if i % 1000000 == 0:
        print(f"Iteration {i}: {date}")
