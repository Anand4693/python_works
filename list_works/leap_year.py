# q3
# display all leap years from list
years = [1900,1901,1991, 1992,1993,1994, 2000,2024, 2021, 2011]

leap_years = [year for year in years if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))]
print(leap_years)