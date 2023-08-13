#
#運行環境: PC, WIN10, VSCODE
#功能:模擬30pcs 溫濕度模組，數據發送到 Thingsboard(Raspberry Pi)
#

import paho.mqtt.client as paho  # mqtt library
import os
import json
import time
from datetime import datetime
import random

ACCESS_TOKEN = 'nnnnnnnnnnn'  # Token of your device
broker = "nnn.nnn.n.nn"  # host name
port = nnnn  # data listening port

#定義30組溫度的鍵值
Temperature_Keys_list=[
'T1','T2','T3','T4','T5','T6','T7','T8','T9','T10',
'T11','T12','T13','T14','T15','T16','T17','T18','T19','T20',
'T21','T22','T23','T24','T25','T26','T27','T28','T29','T30'
]

#定義30組濕度的鍵值
Humidity_Keys_list=[
'RH1','RH2','RH3','RH4','RH5','RH6','RH7','RH8','RH9','RH10',
'RH11','RH12','RH13','RH14','RH15','RH16','RH17','RH18','RH19','RH20',
'RH21','RH22','RH23','RH24','RH25','RH26','RH27','RH28','RH29','RH30'
]

def on_publish(client, userdata, result):  # create function for callback
    print("data published to thingsboard \n")
    pass


client1 = paho.Client("control1")  # create client object
client1.on_publish = on_publish  # assign function to callback
client1.username_pw_set(ACCESS_TOKEN)  # access token from thingsboard device
client1.connect(broker, port, keepalive=60)  # establish connection

Temperature_list=[]
Humidity_list=[]
while True:
    #隨機生成 30組的 溫度值跟濕度值
    Temperature_list.clear()#每次發送前 都先清空Temperature_list
    Humidity_list.clear()#每次發送前 Humidity_list
    for i in range(30):
        x1 = random.uniform(10.0, 50.0)
        x2 = round(x1,1)
        y1 = random.uniform(50, 90)
        y2 = round(y1,1)
        Temperature_list.append(str(x2))
        Humidity_list.append(str(y2))

    #把溫濕度的鍵值跟數值 30組串接在一起 
    payload = "{"
    for i in range(30):
        payload += "\"" 
        payload += Temperature_Keys_list[i]
        payload += "\":" 
        payload += Temperature_list[i]
        payload +=','

        payload += "\"" 
        payload += Humidity_Keys_list[i]
        payload += "\":" 
        payload += Humidity_list[i]
        payload +=','
        
    payload = payload[:-1]#刪除最後一個逗號
    payload += "}"
    
    ret = client1.publish("v1/devices/me/telemetry", payload)  # topic-v1/devices/me/telemetry
    print("Please check LATEST TELEMETRY field of your device")
    time.sleep(5)
