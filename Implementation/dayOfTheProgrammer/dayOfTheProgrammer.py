"""Solution for HackerRank challenge: Day Of The programmer
"""

def day_of_the_programmer(year):
    """Find the Day of the Programmer in Russia,
    given the transition from Julian to Gregorian calendar in 1918
    and accounting for leap year rules in each calendar

    Args:
        year (int): year to find Day of the Programmer

    Returns:
        string: 'dd.mm.yyyy' formatted Day of the Programmer
    """
    leap, total = 0, 256

    #Determine Leap Years
    if year <= 1917 and year >= 1700: # Julian calendar
        if year % 4 == 0:
            leap = 1
    elif year == 1918:
        leap = -13
    elif year >= 1919 and year <= 2700: # Gregorian Calendar
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            leap = 1

    days_in_month = [31, 28 + leap, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Determine month and day
    for i in xrange(len(days_in_month)):
        total -= days_in_month[i]
        if total < 1:
            month = i + 1
            day = total + days_in_month[i]
            break

    # format output into 'dd.mm.yyyy'
    day = '{:02d}'.format(day)
    month = '{:02d}'.format(month)
    yyyy = '{:04d}'.format(year)
    return day + '.' + month + '.' + yyyy

def main():
    """Receives input from stdin, provides output to stdout.
    """
    year = int(raw_input())
    print day_of_the_programmer(year)

if __name__ == '__main__':
    main()
