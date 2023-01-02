import random
import time

from paho.mqtt import client as mqtt_client

broker = 'localhost'
port = 1883
top_temp = "srv/temperature"
top_hum = "srv/humidity"

client_id = f'python-mqtt-{random.randint(0, 1000)}'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
   # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client,topic, msg):
    result = client.publish(topic, msg, qos=2)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")


def run():
    client = connect_mqtt()
    msg_count = 0
    client.loop_start()

    while (True):
        time.sleep(1)
        temperature = 20 + (random.randint(0, 100) * 4)
        msg = f"temperature: {temperature}"
        publish(client, top_temp, msg)

        humidity = (random.randint(0, 100))
        msg = f"humidity: {humidity}"
        publish(client, top_hum, msg)

        msg_count += 1

run()
