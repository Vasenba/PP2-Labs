from datetime import date, timedelta

y = date.today() + timedelta(1)
x = date.today()
z = date.today() - timedelta(1)
print(y,x,z)
