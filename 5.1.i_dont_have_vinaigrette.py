import datetime
import random


# The function receives two dates and extracts a date between them,
# and if it comes out on Monday, prints a corresponding message
def between_dates(first1_date, second1_date):
    # Conversion of the dates from a string to a date
    datetime_first = datetime.datetime.strptime(first1_date, '%Y-%m-%d').date()
    datetime_second = datetime.datetime.strptime(second1_date, '%Y-%m-%d').date()

    num_days = (datetime_second - datetime_first).days  # The number of days between the dates
    rand_days = random.randint(1, num_days)  # A random number in the range of the number of days between the two dates
    random_date = datetime_first + datetime.timedelta(days=rand_days)
    x = random_date.weekday()  # The day of the week when the random date (Monday = 0)

    # Checking if it`s monday
    if x == 0:
        print("I don`t have vinaigrette")
    print(random_date)


first_date = input()  # First input from user
second_date = input()  # Second input from user
between_dates(first_date, second_date)
