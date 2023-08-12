"""Generates a random date between two given dates

This script allows the user to enter 2 dates in the format 'YYYY-MM-DD'
and generate a random date between them, and checks if it's a Monday. If
so, prints a corresponding message, otherwise prints the generated date.

This file contains the following functions:

    * between_dates - the main function of the script
"""

import datetime
import random


def between_dates(first1_date: str, second1_date: str):
    """Gets two dates and extracts a date between them,
       and if it comes out on Monday, prints a corresponding message """

    datetime_first = datetime.datetime.strptime(first1_date, '%Y-%m-%d').date()
    datetime_second = datetime.datetime.strptime(second1_date, '%Y-%m-%d').date()

    number_days = (datetime_second - datetime_first).days
    # A random number in the range of the number of days between the two dates
    rand_days = random.randint(1, number_days)
    random_date = datetime_first + datetime.timedelta(days=rand_days)
    week_day = random_date.weekday()  # The day of the week when the random date (Monday = 0)

    if week_day == 0:
        print("I don`t have vinaigrette")
    print(random_date)


if __name__ == '__main__':
    first_date = input()
    second_date = input()
    between_dates(first_date, second_date)
