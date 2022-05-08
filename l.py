import datetime
from pickle import FALSE, TRUE
import sys
import time
from Adafruit_IO import MQTTClient
import serial.tools.list_ports
import serial
import threading
import json
import requests

AIO_USERNAME = "Airforce"
AIO_KEY = "aio_gBjJ28UyNtMGzOv4gsoPkrfdv87H"
        
def update():
    while True:
        watering = False
        alert = False
        if Heat>(conditionHeatAvg+2) or Heat < (conditionHeatAvg-2):
            # client.publish("Watering",1) 
            watering = True
        elif Heat>(conditionHeatAvg+5) or Heat < (conditionHeatAvg-5):
            # ser.write(("B#").encode()) 
            # client.publish("Watering",1) 
            alert = True
            
        if Humd>(conditionHumdAvg+2) or Humd < (conditionHumdAvg-2):
            watering = True 
        elif Humd>(conditionHumdAvg+5) or Humd < (conditionHumdAvg-5):
            alert = True
            
        if Earth>(conditionEarthAvg+2) or Earth < (conditionEarthAvg-2):
            watering = True 
        elif Earth>(conditionEarthAvg+5) or Earth < (conditionEarthAvg-5):
            alert = True
            
        if Time1 == str(datetime.datetime.now().strftime("%X"))[0:5]:
            watering = True 

        if Time2 == str(datetime.datetime.now().strftime("%X"))[0:5]:
            watering = True 

        if watering == True:
            client.publish("Watering",1) 
        if alert == True:
            ser.write(("B#").encode()) 
            client.publish("Watering",1) 
        if watering == False:
            client.publish("Watering",0)  

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

mess = ""
bbc_port = ""
if len(bbc_port) > 0:
    ser = serial.Serial(port=bbc_port, baudrate=115200)
Time1 = json.loads(requests.request("GET", "https://io.adafruit.com/api/v2/Airforce/feeds/mark1/data?limit=1", headers= {'X-AIO-Key': AIO_KEY}).text)[0]['value']
Time2 = json.loads(requests.request("GET", "https://io.adafruit.com/api/v2/Airforce/feeds/mark2/data?limit=1", headers= {'X-AIO-Key': AIO_KEY}).text)[0]['value']      
ConditionalHeat = json.loads(requests.request("GET", "https://io.adafruit.com/api/v2/Airforce/feeds/conditionheat/data?limit=1", headers= {'X-AIO-Key': AIO_KEY}).text)[0]['value']      
ConditionalHumd = json.loads(requests.request("GET", "https://io.adafruit.com/api/v2/Airforce/feeds/conditionalhumd/data?limit=1", headers= {'X-AIO-Key': AIO_KEY}).text)[0]['value']      
ConditionalEarth = json.loads(requests.request("GET", "https://io.adafruit.com/api/v2/Airforce/feeds/conditionalearth/data?limit=1", headers= {'X-AIO-Key': AIO_KEY}).text)[0]['value']        
print(ConditionalHeat)
conditionHeatAvg = (ConditionalHeat.split("-")[0] + ConditionalHeat.split("-")[1])/2
conditionHumdAvg = (ConditionalHumd.split("-")[0] + ConditionalHumd.split("-")[1])/2
conditionEarthAvg = (ConditionalEarth.split("-")[0] + ConditionalEarth.split("-")[1])/2
Heat= 30
Humd= 30
Earth = 30
threading.Thread(target=update).start()

while True :
    # readSerial()
    time . sleep (15)