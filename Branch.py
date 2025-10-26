import datetime

today = datetime.date.today().day
if today % 2 == 1:
    print("Hello New Branch")
else:
    print("Bye New Branch")
