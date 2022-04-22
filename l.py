import datetime
import sys
import pyrebase
import time
from Adafruit_IO import MQTTClient
import serial.tools.list_ports
import serial
import threading
AIO_FEED_ID = "Watering"
AIO_USERNAME = "Airforce"
AIO_KEY = "aio_Qcan99Ot2yY7cMOLDjlyHeNhbm1t"

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
def update():
    while True:
        time.sleep(100)
        mark = str(datetime.now().date())+"-"+str(datetime.now().hour)+"-"+str(datetime.now().minute)
        data= {"Heat":Heat, "Humd": Humd, "Earth": Earth}
        db.push(data)
        db.child("Minute").child(mark).set(data)
        time.sleep(60)
        
def update2():
    while True:
        time.sleep(100)
        mark = str(datetime.now().date())
        data= {"Heat":Heat, "Humd": Humd, "Earth": Earth}
        db.push(data)
        db.child("Day").child(mark).set(data)
        time.sleep(3600*24)
        


def processData(data):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    if splitData[0]==1:
        client.publish("Heat",splitData[1])
        if splitData[1] < ConditionalHeat:
            ser.write(("B#").encode()) 
    if splitData[0]==2:
        client.publish("Humd",splitData[1])
        if splitData[1] < ConditionalHumd:
            ser.write(("B#").encode()) 
    if splitData[0]==3: 
        client.publish("Earth",splitData[1])  
        if splitData[1] < ConditionalEarth:
            ser.write(("B#").encode())  

def readSerial():
    bytesToRead = ser.inWaiting()
    if (bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")
        while ("#" in mess) and ("!" in mess):
            start = mess.find("!")
            end = mess.find("#")
            processData(mess[start:end + 1])
            if (end == len(mess)):
                mess = ""
            else:
                mess = mess[end+1:]

def connected ( client ) :
    print ("Ket noi thanh cong ...")
    client.subscribe("mark1")
    client.subscribe("mark2")
    client.subscribe("ConditionHeat")
    client.subscribe("ConditionalHumd")
    client.subscribe("ConditionalEarth")

def subscribe ( client , userdata , mid , granted_qos ):
    print (" Subcribe thanh cong ...")

def disconnected ( client ) :
    print (" Ngat ket noi ...")
    sys . exit (1)

def message ( client , feed_id , payload ):
    global ConditionalHeat
    global ConditionalHumd
    global ConditionalEarth
    global Time1
    global Time2 

    print (" Nhan du lieu : " + payload )
    if feed_id=="mark1":
        Time1 = payload
    if feed_id=="mark2":
        Time2 = payload
    if feed_id=="ConditionHeat":
        ConditionalHeat0 = payload.split("-")[0]
        ConditionalHeat1 = payload.split("-")[1]
    if feed_id=="ConditionalHumd":
        ConditionalHumd0 = payload.split("-")[0]
        ConditionalHumd1 = payload.split("-")[1]
    if feed_id=="ConditionalEarth":
        ConditionalEarth0 = payload.split("-")[0]
        ConditionalEarth1 = payload.split("-")[1]
    if feed_id == "Watering":
        if payload == 1:
            ser.write(("A#").encode()) 
            client.publish("Watering",1) 
        if payload == 2:
            ser.write(("B#").encode()) 
            client.publish("Watering",1)

client = MQTTClient ( AIO_USERNAME , AIO_KEY )
client . on_connect = connected
client . on_disconnect = disconnected
client . on_message = message
client . on_subscribe = subscribe
client . connect ()
client . loop_background ()
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
mess = ""
bbc_port = ""
if len(bbc_port) > 0:
    ser = serial.Serial(port=bbc_port, baudrate=115200)
ConditionalHeat0 = db.child("User").child("ConditionHeat").get().val().split("-")[0]
ConditionalHumd0 = db.child("User").child("ConditionHeat").get().val().split("-")[1]
ConditionalEarth0 = db.child("User").child("ConditionHumd").get().val().split("-")[0]
ConditionalHeat1 = db.child("User").child("ConditionHumd").get().val().split("-")[1]
ConditionalHumd1 = db.child("User").child("ConditionEarth").get().val().split("-")[0]
ConditionalEarth1 = db.child("User").child("ConditionEarth").get().val().split("-")[1]
Time1 = "nan"
Time2 = "nan"      
Heat = 30
Humd = 30
Earth =30   
firebase = pyrebase.initialize_app(config)

db = firebase.database()
threading.Thread(target=update).start()
threading.Thread(target=update2).start()
while True :
    readSerial()
    time . sleep (30)
    # if Heat>ConditionalHeat:
    #     client.publish("Watering",1) 
    # elif Heat<ConditionalHeat-5:
    #     ser.write(("B#").encode()) 
    #     client.publish("Watering",1) 
    # elif Humd<ConditionalHumd:
    #     client.publish("Watering",1)  
    # elif Earth<ConditionalEarth:
    #     client.publish("Watering",1) 
    # elif Time1 == str(datetime.datetime.now().strftime("%X"))[0:5]:
    #     client.publish("Watering",1) 
    # elif Time2 == str(datetime.datetime.now().strftime("%X"))[0:5]:
    #     ser.write(("A#").encode()) 
    #     client.publish("Watering",1)  
    # else:
    #     client.publish("Watering",0)  