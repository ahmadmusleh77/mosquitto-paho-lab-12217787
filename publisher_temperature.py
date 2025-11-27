import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client(
    client_id="TempPublisher_12217787",
    callback_api_version=mqtt.CallbackAPIVersion.VERSION1
)

client.connect("localhost", 1883, 60)

while True:
    temp = random.uniform(20, 30)
    message = f"Temperature: {temp:.2f} | Ahmad Musleh | 12217787"
    client.publish("room/temperature", message)
    print("Sent:", message)
    time.sleep(2)
