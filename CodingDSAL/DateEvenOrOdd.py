def is_even_date(date):
    """Returns True if the given date is even, False otherwise."""
    year, month, day = date.split("-")
    year = int(year)
    day = int(day)
    if month in ["04", "06", "09", "11"]:
        return day % 2 == 0
    elif month in ["02"]:
        if year % 4 == 0:
            return day % 2 == 0
        else:
            return day % 2 != 0
    else:
        return day % 2 != 0


def main():
    """Gets a date from the user and prints whether it is even or odd."""
    date = input("Enter a date in the format YYYY-MM-DD: ")
    if is_even_date(date):
        print(f"{date} is an even date.")
    else:
        print(f"{date} is an odd date.")


if __name__ == "__main__":
    main()
