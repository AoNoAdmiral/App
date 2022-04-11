import serial
import paho.mqtt.client as mqtt
import time
import json
import threading

THINGSBOARD_HOST = "demo.thingsboard.io"
ACCESS_TOKEN = 'LyoSMl8n9Yoki1fBpJoj'   
request = {"method": "check1", "params": {}}


def update():
    while True:
        client.publish('v1/devices/me/rpc/request/1',json.dumps(request), 1)
        time.sleep(100)

def on_connect(client, userdata, flags, rc):
    print("rc code:", rc)
    client.subscribe('v1/devices/me/rpc/response/1')
    

def on_message(client, userdata, msg):
    print('Topic: ' + msg.topic + '\nMessage: ' + msg.payload.decode("utf-8"))
    r =   json.loads(msg.payload.decode("utf-8"))
    #dk
    # r luu dk tuoi tu dong. No print message khi chay nen may biet dang data
    # ko biet nhan t
    watering = 1

watering = 0
client = mqtt.Client()    
client.loop_start()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGSBOARD_HOST, 1883,60)

threading.Thread(target=update).start()

#time lay bang
import datetime
# hour = datetime.now().hour() -> Nho cong 7 roi mod 24 ( no lay h 0 va minh h bay)
# min = datetime.now().minute()

ser = serial.Serial('COM4', 19200)
while  True:
    # lay data
    if watering:
        #tuoi cay
        pass
    else:
        #show bang
        pass


        




