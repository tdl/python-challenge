import calendar

for i in range(0, 10):
    year = "1" + str(i) + "6"

    ## check which years have january starting on a thursday
    ## and are also leapyears
    if calendar.weekday(int(year), 1, 1) == 3 \
        and calendar.isleap(int(year)):
        print year

for i in range(0, 100):
    year = ""
    if len(str(i)) == 1:
        year = "10" + str(i) + "6"
    else :
        year = "1" + str(i) + "6"

    if calendar.weekday(int(year), 1, 1) == 3 \
        and calendar.isleap(int(year)):
        print year
    
