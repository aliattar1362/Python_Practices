"""
Program asks user to enter month,
year and the weekday of the first day of the month
and then prints a calendar which looks like this:

  2020-09
  Mo Tu We Th Fr Sa Su
      1  2  3  4  5  6
   7  8  9 10 11 12 13
  14 15 16 17 18 19 20
  21 22 23 24 25 26 27
  28 29 30
"""

def read_inputs():
    yyyy = read_integer("Enter the year", 1900, 2500)
    mm = read_integer("Enter the month", 1, 12)
    weekday = read_integer("The 1st weekday (0 = Mon, 1 = Tue, etc.)", 0, 6)

    return mm, yyyy, weekday


def read_integer(prompt, minval, maxval):
    while True:
        result = int(input(f"{prompt} [{minval}-{maxval}] "))

        if minval <= result <= maxval:
            return result
        else:
            print(f"You entered a bad value (must be between {minval}-{maxval})")


def print_calendar(mm, yyyy, start_wday):
    MON, SUN = 0, 6

    print(f"{yyyy}-{mm:02d}")
    print("Mo Tu We Th Fr Sa Su")

    print(" " * 3 * start_wday, end="")

    number_of_days = calculate_month_length(mm, yyyy)
    current_wday = start_wday

    for day in range(1, number_of_days + 1):
        print(f"{day:2} ", end="")

        if current_wday == SUN:
            print()
            current_wday = MON
        else:
            current_wday += 1


def calculate_month_length(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif is_leap_year(year):
        return 29
    else:
        return 28


def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def main():
    month, year, starting_weekday = read_inputs()
    print_calendar(month, year, starting_weekday)


if __name__ == "__main__":
    main()
