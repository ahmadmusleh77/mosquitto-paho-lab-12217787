import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client(
    client_id="HumidityPublisher_12217787",
    callback_api_version=mqtt.CallbackAPIVersion.VERSION1
)

client.connect("localhost", 1883, 60)

while True:
    hum = random.uniform(40, 80)
    message = f"Humidity: {hum:.2f} | Ahmad Musleh | 12217787"
    client.publish("room/humidity", message)
    print("Sent:", message)
    time.sleep(2)
