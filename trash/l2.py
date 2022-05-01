import sys
import time
import random
from Adafruit_IO import MQTTClient
import serial.tools.list_ports
import serial
import json
AIO_FEED_ID = "Watering"
AIO_USERNAME = "Airforce"
AIO_KEY = "aio_Hncl31kfAQrNu1qyRmoTruGYqp6M"



def processData(data):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    if splitData[0]==1:
        client.publish("Heat",splitData[1])
    if splitData[0]==2:
        client.publish("Humd",splitData[1])
    if splitData[0]==3: 
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
    client . subscribe ( "Watering" )
    client . subscribe ( "Total" )

def subscribe ( client , userdata , mid , granted_qos ):
    print (" Subcribe thanh cong ...")

def disconnected ( client ) :
    print (" Ngat ket noi ...")
    sys . exit (1)

def message ( client , feed_id , payload ):
    print(feed_id)
    print (" Nhan du lieu : " + payload )
    if len(bbc_port) > 0:
        ser.write((str(message) + "#").encode())

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
while True :
    client.publish("Heat",random.randrange(30, 40, 1))
    client.publish("EarthHumd",random.randrange(70, 90, 1))
    client.publish("Earth",random.randrange(40, 60, 1))
    time . sleep (60)