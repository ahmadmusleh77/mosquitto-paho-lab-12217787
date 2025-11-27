import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print("Temperature Subscriber Received:", msg.payload.decode())

client = mqtt.Client(
    client_id="TempSub_12217787",
    callback_api_version=mqtt.CallbackAPIVersion.VERSION1
)

client.on_message = on_message
client.connect("localhost", 1883, 60)
client.subscribe("room/temperature")

print("Temperature Subscriber Started (Ahmad Musleh - 12217787)")
client.loop_forever()
