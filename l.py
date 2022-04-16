import sys
import time
import random
from Adafruit_IO import MQTTClient
import serial.tools.list_ports
import serial
import json
AIO_FEED_ID = "Watering"
AIO_USERNAME = "Airforce"
AIO_KEY = "aio_Qmkq90BKruJ2NFxaiehyybaxirPu"

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
    client.subscribe(AIO_FEED_ID)

def subscribe ( client , userdata , mid , granted_qos ):
    print (" Subcribe thanh cong ...")

def disconnected ( client ) :
    print (" Ngat ket noi ...")
    sys . exit (1)

def message ( client , feed_id , payload ):
    print (" Nhan du lieu : " + payload )
    msg = payload.split("#")
    if len(bbc_port) > 0:
        if msg[0]=="1":
            ser.write(("A#").encode()) 
        data = json.loads (msg[1])
        global ConditionalHeat
        global ConditionalHumd
        global ConditionalEarth
        ConditionalHeat = data["ConditionHeat"]
        ConditionalHumd = data["ConditionalHumd"]
        ConditionalEarth = data["ConditionalEarth"]

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
ConditionalHeat = 80 
ConditionalHumd = 80    
ConditionalEarth = 80       
while True :
    readSerial()
    time . sleep (30)