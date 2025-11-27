Mosquitto + Paho MQTT Lab – Ahmad Musleh (12217787)
-
This project demonstrates how to use the Mosquitto MQTT Broker together with Paho MQTT (Python) to simulate IoT data publishing and subscribing for three different topics:
Temperature
Humidity
People Count
All scripts are written in Python and tested on Windows using a local Mosquitto broker.


Project Structure
-
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
      
 ----------------------------------------------------------------   
How to Run the Project
-
1. Start the Mosquitto Broker:net start mosquitto   || run manually:cd "C:\Program Files\mosquitto" --->    .\mosquitto -v
2. Install Paho MQTT:pip install paho-mqtt
3. Run the Publishers:
    python publisher_temperature.py
    python publisher_humidity.py
    python publisher_people.py
4. Run the Subscribers:
   python subscriber_temperature.py
   python subscriber_humidity.py
   python subscriber_people.py


---------------------------------------------------------
Student Information:
-
Name: Ahmad Musleh
ID: 12217787
Course: Io T--> Lab: Mosqitto + Paho

----------------------------------------------------------
Screenshots: All screenshots of publishers, subscribers, and broker outputs are included in the /Screenshot/ folder.
-
----------------------------------------------------------
What This Lab Demonstrates:
-
. Setting up Mosquitto on Windows
. Publishing sensor data using Paho MQTT
. Subscribing and receiving data in real time
. Running multiple MQTT topics simultaneously
. Understanding basic IoT communication concepts

---------------------------------------------------------
Notes:
-
. All code works with Paho v2.1.0
. Broker runs on localhost:1883
. This project simulates data (no physical sensors needed)
