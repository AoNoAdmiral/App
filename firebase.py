
import pyrebase


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

data = {"Heta":67, "Name": "Nhat", "Staff": True}

#----------------------------------------
#create data

#db.push(data)
# db.child("User").child("second").set(data)

DuLieu = db.child("User").get()
print(DuLieu.val())
