import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client(
    client_id="PeoplePublisher_12217787",
    callback_api_version=mqtt.CallbackAPIVersion.VERSION1
)

client.connect("localhost", 1883, 60)

while True:
    people = random.randint(0, 20)
    message = f"People Count: {people} | Ahmad Musleh | 12217787"
    client.publish("room/people", message)
    print("Sent:", message)
    time.sleep(2)
