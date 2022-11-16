 # publish

import paho.mqtt.client as paho
import json

#broker = "localhost"
broker = "10.20.1.95"  #publish on other user's broker 


data = {'LubabaFirst': 'first', 'LubabaSecond':'last', 'AnInteger':201415}

client = paho.Client()
client.connect(broker, 1883)

client.publish("alfaisal/lubaba", payload=json.dumps(data))