import datetime


print(datetime.datetime.strptime(str(datetime.datetime.now().strftime("%X"))[0:5],"%H:%M")-datetime.datetime.strptime("22:15","%H:%M")<=datetime.timedelta(minutes=5))