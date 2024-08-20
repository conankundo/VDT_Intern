# python 3.11

import random
import time
import json
import paho.mqtt.client as mqtt_client


broker = 'mqttvcloud.innoway.vn'
port = 1883
topic = "innoway/pub2sv"
# topic = "innoway/pub2here"
# Generate a Client ID with the publish prefix.
client_id = f'publish-{random.randint(0, 1000)}'
username = 'dac'
password = 'XY3eG20P0P6rMvXC8dejf15iyae9Gait'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("PUB Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = 1
    # payloadData = {
    #     "key": "77bb52ba-08f3-4e1f-8158-80a80b570dcc",
    #     "status": "check from python"
    # }
    payloadData = {
        "id": "aa140a43-e61e-4c43-8a41-0a108a8e7cd2",
        "status": "1",
        "adapter_id": "e7c06ba7-6d56-48eb-a2e4-d099846d4a02",
        "createdBy": "d7a55498-4fba-4162-bff6-3806f936622f",
        "destination": "adapter-2"
    }
    while True:
        time.sleep(1)
        msg = json.dumps(payloadData, indent = 2)
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Sent {msg} to topic {topic}")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1
        if msg_count > 1:
            break

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)
    client.loop_stop()


if __name__ == '__main__':
    run()
