 # publish

import paho.mqtt.client as paho
import json

#broker = "localhost"
#broker = "10.54.27.114"  #publish on other user's broker 
#broker = "broker.emqx.io"  #virtual broker

broker = "broker.hivemq.com"  #virtual broker

data = {'LubabaFirst': 'first', 'LubabaSecond':'last', 'AnInteger':201415}

client = paho.Client()
client.connect(broker, 1883)

client.publish("lubaba", payload=json.dumps(data))