#subscribe

import paho.mqtt.client as paho
import json

#broker = "localhost"
#broker = "10.54.27.114"

broker = "broker.emqx.io"  #virtual broker

def is_json(myjson):
  try:
    json.loads(myjson)
  except ValueError as e:
    return False
  return True

def on_message(client, userdata, msg):
    message = msg.payload
    if is_json(message):
        new_bytes_start = json.loads(message.decode("utf-8"))
        print("Name: ", new_bytes_start["Name"])
        print("Last Name: ", new_bytes_start["SecondName"])
        print("Integer: ", new_bytes_start["NN"])
    else:
        print("The receives message is not a valid JSON")

client = paho.Client()
client.on_message = on_message
client.connect(broker, 1883)
client.subscribe("alfaisal/lubaba")
#client.subscribe("#") subsicribe for all tites on this broker

client.loop_forever()

