import datetime

today = datetime.date.today().day
if today%2==1:
    print("Hello Git")
else:
    print("Bye Git")