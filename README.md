# Mosquitto + Paho MQTT Lab – Ahmad Musleh (12217787)

This project demonstrates how to use the Mosquitto MQTT Broker together with Paho MQTT (Python) to simulate IoT data publishing and subscribing for three different topics: Temperature, Humidity, and People Count.  
All scripts are written in Python and tested on Windows using a local Mosquitto broker.

---

## Project Structure
```
mosqqito/
│
├── publisher_temperature.py
├── publisher_humidity.py
├── publisher_people.py
│
├── subscriber_temperature.py
├── subscriber_humidity.py
├── subscriber_people.py
│
└── Screenshot/
      ├── Mosquitto Broker.png
      ├── publisher_temperature_Screenshot.png
      ├── publisher_humidity_Screenshot.png
      ├── publisher_people_Screenshot.png
      ├── subscriber_temperature_Screenshot.png
      ├── subscriber_humidity_Screenshot.png
      └── subscriber_people_Screenshot.png
```

---

## How to Run the Project

### 1. Start the Mosquitto Broker
Using Windows service:
```
net start mosquitto
```

Or manually:
```
cd "C:\Program Files\mosquitto"
.\mosquitto -v
```

### 2. Install Paho MQTT
```
pip install paho-mqtt
```

### 3. Run the Publishers
```
python publisher_temperature.py
python publisher_humidity.py
python publisher_people.py
```

### 4. Run the Subscribers
```
python subscriber_temperature.py
python subscriber_humidity.py
python subscriber_people.py
```

---

## Student Information
Name: Ahmad Musleh  
ID: 12217787  
Course: IoT Laboratory – Mosquitto + Paho MQTT

---

## Additional Notes
- All scripts were tested using Paho v2.1.0.  
- The Mosquitto broker is running locally on port **1883**.  
- The project simulates sensor data; no physical sensors were required.  
- All screenshots (publishers, subscribers, and broker) are included in the **Screenshot** folder.

