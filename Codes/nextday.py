import stdio

stdio.write("Input a year: ")
year = stdio.readInt()

stdio.write("Input a month [1-12]: ")
month = stdio.readInt()

month_length = 30
if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if ((year % 4 == 0 and year != 100 ==0) or year % 400 == 0):
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30

stdio.write("Input a day [1-31]: ")
day = stdio.readInt()

if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1

stdio.writeln("The next date is [yyyy-mm-dd] " \
    + str(year) + " "\
    + str(month) + " "\
    + str(day)) 