"""Working with datetime module"""
import datetime


def days_in_month(year=None, month=None):
    """
       Inputs:
         year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
                 representing the year
         month - an integer between 1 and 12 representing the month

       Returns:
         The number of days in the input month.
       """
    leap = False
    if month == 2:
        if year % 4 == 0:
            leap = True
            if year % 100 == 0:     # On The Basis of Gregorian Calendar criteria
                leap = False
                if year % 400 == 0:
                    leap = True
        return leap + 28
    lst = [1, 3, 5, 7, 8, 10, 12]       # list holds all months which have 31 days
    if month in lst:
        return 31
    return 30


def is_valid_date(year, month, day):
    """
       Inputs:
         year  - an integer representing the year
         month - an integer representing the month
         day   - an integer representing the day

       Returns:
         True if year-month-day is a valid date and
         False otherwise
       """
    cond1 = datetime.MINYEAR <= year <= datetime.MAXYEAR
    cond2 = 1 <= month <= 12
    cond3 = 0 <= day <= days_in_month(year, month) and day != 0
    return cond1 and cond2 and cond3


def days_between(year1, month1, day1, year2, month2, day2):
    """
        Inputs:
          year1  - an integer representing the year of the first date
          month1 - an integer representing the month of the first date
          day1   - an integer representing the day of the first date
          year2  - an integer representing the year of the second date
          month2 - an integer representing the month of the second date
          day2   - an integer representing the day of the second date

        Returns:
          The number of days from the first date to the second date.
          Returns 0 if either date is invalid or the second date is
          before the first date.
        """
    if is_valid_date(year1, month1, day1) and is_valid_date(year2, month2, day2):
        var = datetime.date(year2, month2, day2) - datetime.date(year1, month1, day1)
        var = str(var)
        if var != '0:00:00':
            var = int(var.split()[0])
            if var > 0:
                return var
    return 0


def age_in_days(year, month, day):
    """
       Inputs:
         year  - an integer representing the birthday year
         month - an integer representing the birthday month
         day   - an integer representing the birthday day

       Returns:
         The age of a person with the input birthday as of today.
         Returns 0 if the input date is invalid of if the input
         date is in the future.
       """
    today = str(datetime.datetime.now()).split(" ")[0]
    year2, month2, day2 = today.split("-")
    days = days_between(year, month, day, int(year2), int(month2), int(day2))
    if days > 0:
        return days
    return 0


year = int(input("Enter your birth year :- "))
month = int(input("Enter your birth month :- "))
day = int(input("Enter your birth day :- "))
print(age_in_days(year, month, day))
