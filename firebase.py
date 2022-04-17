
import pyrebase
import time
from datetime import datetime

# import data_upload_db

config = {
  "apiKey": "AIzaSyBvSDvuuBcheDg6fZUpi30Il-MUogLKwV4",
  "authDomain": "chill-2ddd1.firebaseapp.com",
  "databaseURL": "https://chill-2ddd1-default-rtdb.firebaseio.com",
  "projectId": "chill-2ddd1",
  "storageBucket": "chill-2ddd1.appspot.com",
  "messagingSenderId": "62414238957",
  "appId": "1:62414238957:web:04d88c13d1ac0510a808e4",
  "measurementId": "G-ZG9Z0XL8MW"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()



#----------------------------------------
#create data

# counter_5_minute = 0;
# counter_1_day = 0

# def upload_db():
#     global counter_5_minute
#     global counter_1_day

#     for showdata in data_upload_db.data:

#         if counter_5_minute==0:
#             mark = str(datetime.now().date())+"-"+str(datetime.now().hour)+"-"+str(datetime.now().minute)
#             db.push(data_upload_db.data[showdata])
#             db.child("User").child(mark).set(data_upload_db.data[showdata])

#         if counter_1_day>=0:
#             mark2 = str(datetime.now().date())
#             db.push(data_upload_db.data[showdata])
#             db.child("User").child(mark2).set(data_upload_db.data[showdata])

#         counter_5_minute = (counter_5_minute + 1) % 5;
#         counter_1_day = (counter_1_day + 1) % 1440;
#         time.sleep(60)

# upload_db()

data = {"Heat":74, "Humd": 60, "Earth": 40}
db.child("Minute").child('2022-04-16-6-45').set(data)
# db.push(data)

DuLieu = db.child("Minute").get()
for x, y in DuLieu.val().items():
   print(x, y)