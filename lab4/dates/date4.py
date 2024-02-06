import datetime

def seconds(date1,date2):
    date = date2 - date1
    return date.total_seconds()

date3 = datetime.datetime(2024,2,7,0,0,0)
date4 = datetime.datetime.now()
x = seconds(date3,date4)
print(x)
