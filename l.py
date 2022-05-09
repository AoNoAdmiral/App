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
AIO_KEY = "aio_jhEv983rGTulINXBKuEds5KkS1FW"
        
def update():
    while True:
        watering = True
        alert = False
        if Heat>int(ConditionalHeat.split("-")[1]):
            watering = True
        elif Heat < int(ConditionalHeat.split("-")[0]):
            alert = True
            
        if Humd>int(ConditionalHumd.split("-")[1]):
            watering = True 
        elif Humd < int(ConditionalHumd.split("-")[0]):
            alert = True
            
        if Earth>int(ConditionalEarth.split("-")[1]):
            watering = True 
        elif Earth < int(ConditionalEarth.split("-")[0]):
            alert = True
        
        if datetime.datetime.strptime(str(datetime.datetime.now().strftime("%X"))[0:5],"%H:%M")-datetime.datetime.strptime(Time1,"%H:%M")<=datetime.timedelta(minutes=5):
            print("Hello")
            watering = True 

        if datetime.datetime.strptime(str(datetime.datetime.now().strftime("%X"))[0:5],"%H:%M")-datetime.datetime.strptime(Time2,"%H:%M")<=datetime.timedelta(minutes=5):
            watering = True 

        if watering == True:
            client.publish("Watering",1) 
            ser.write(("A#").encode())
        if alert == True:
            ser.write(("B#").encode()) 
        if watering == False:
            client.publish("Watering",0)  
        time.sleep(15)
            
def processData(data):
    print(data)
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    if splitData[0]=="1":  
        client.publish("Heat",splitData[1]) 
    if splitData[0]=="2":
        client.publish("Humd",splitData[1])
    if splitData[0]=="3": 
        client.publish("Earth",splitData[1])  

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
    client.subscribe("Watering")

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
        ConditionalHeat = payload
    if feed_id=="ConditionalHumd":
        ConditionalHumd = payload
    if feed_id=="ConditionalEarth":
        ConditionalEarth = payload


client = MQTTClient ( AIO_USERNAME , AIO_KEY )
client . on_connect = connected
client . on_disconnect = disconnected
client . on_message = message
client . on_subscribe = subscribe
client . connect ()
client . loop_background ()

mess = ""
bbc_port = "COM11"
if len(bbc_port) > 0:
    ser = serial.Serial(port=bbc_port, baudrate=115200)
Time1 = json.loads(requests.request("GET", "https://io.adafruit.com/api/v2/Airforce/feeds/mark1/data?limit=1", headers= {'X-AIO-Key': AIO_KEY}).text)[0]['value']
Time2 = json.loads(requests.request("GET", "https://io.adafruit.com/api/v2/Airforce/feeds/mark2/data?limit=1", headers= {'X-AIO-Key': AIO_KEY}).text)[0]['value']      
ConditionalHeat = json.loads(requests.request("GET", "https://io.adafruit.com/api/v2/Airforce/feeds/conditionheat/data?limit=1", headers= {'X-AIO-Key': AIO_KEY}).text)[0]['value']      
ConditionalHumd = json.loads(requests.request("GET", "https://io.adafruit.com/api/v2/Airforce/feeds/conditionalhumd/data?limit=1", headers= {'X-AIO-Key': AIO_KEY}).text)[0]['value']      
ConditionalEarth = json.loads(requests.request("GET", "https://io.adafruit.com/api/v2/Airforce/feeds/conditionalearth/data?limit=1", headers= {'X-AIO-Key': AIO_KEY}).text)[0]['value']        
Heat= 30
Humd= 30
Earth = 30
threading.Thread(target=update).start()

while True :
    readSerial()
    time . sleep (15)