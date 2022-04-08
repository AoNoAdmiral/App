import serial
import paho.mqtt.client as mqtt
import time
import json

THINGSBOARD_HOST = "demo.thingsboard.io"
ACCESS_TOKEN = 'LyoSMl8n9Yoki1fBpJoj'   
request = {"method": "gettelemetry", "params": {}}

def on_connect(client, userdata, flags, rc):
    print("rc code:", rc)
    client.subscribe('v1/devices/me/rpc/response/+')

def on_message(client, userdata, msg):
    print('Topic: ' + msg.topic + '\nMessage: ' + msg.payload.decode("utf-8"))

client = mqtt.Client()    
client.loop_start()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGSBOARD_HOST, 1883,60)


ser = serial.Serial('COM4', 19200)
# while  True:
#     while ser.in_waiting:
#         data_in = ser.readline()
#         print(data_in)
#         client.publish('v1/devices/me/telemetry', json.dumps(data_in), 1)

while True:
    client.publish('v1/devices/me/rpc/request/1',json.dumps(request), 1)
    time.sleep(5)
        




