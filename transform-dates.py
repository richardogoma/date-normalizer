#!/usr/bin/env python3
import re
from datetime import datetime


def convert_month_year(match):
    month, year = match.groups()
    date = f"{month[:3]}-{year}"
    parsed_date = datetime.strptime(date, "%b-%y")
    return parsed_date.date()


def convert_date(match):
    day, month, year = match.groups()
    date = f"{month}-{day}-{year}"
    parsed_date = datetime.strptime(date, "%m-%d-%Y")
    return parsed_date.date()


def normalize_date(date):
    patterns = [
        (re.compile(r"^([a-zA-Z]{3,})\-*([0-9]{2})$"), convert_month_year),
        (re.compile(r"^(\d{2})\.(\d{2})\.(\d{4})$"), convert_date),
    ]
    for pattern, action in patterns:
        match = pattern.match(date)
        if match:
            result = action(match)
            break
        else:
            result = None
    return result


def main():
    dates = ["January--23", "Aug94", "Febr-22", "26.08.1994"]
    normalized_dates = [normalize_date(datum).strftime("%m-%d-%Y") for datum in dates]
    print(f"Raw dates: {dates} \nNormalized_dates: {normalized_dates}")


if __name__ == "__main__":
    main()
