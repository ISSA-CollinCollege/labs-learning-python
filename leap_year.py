# Requirements for a leap year:
# 1. Must be evenly divisble by 4
# 2. Cannot by evenly divisble by 100, unless it is divisible by 400

year = int(input("Enter a year to see if it is or will be a leap year: \n"))

def leap_year(year):
    if year % 4 == 0 and (year % 100 !=0 or year % 400 == 0):
        print(f"{year} is a leap year!")
    else:
        print(f"{year} is not a leap year.")

leap_year(year)