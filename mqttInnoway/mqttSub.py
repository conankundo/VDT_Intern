# python 3.11
import random
import paho.mqtt.client as mqtt_client
from decrypt_final import *

## infor
broker = 'mqttvcloud.innoway.vn'
port = 1883
topic = ["innoway/pubDownHere","innoway/sv2ue"]

# Generate a Client ID with the publish prefix.
client_id = f'publish-{random.randint(0, 1000)}'
username = 'adapter-id'
password = 'XY3eG20P0P6rMvXC8dejf15iyae9Gait'
AESkey = ['pA2WG0J4g8XYR71z']

#global var
all_msg = ""
step = -1

def connect_mqtt():
    def on_connect(client, userdata,flags, rc):
        if rc == 0:
            print("SUB Connected to MQTT Broker!")
    def on_disconnect(client, userdata,flags, rc):
        if rc != 0:
            print("Unexpected MQTT disconnection. Will auto-reconnect")

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    client.on_disconnect = on_disconnect
    return client


def subscribe(client: mqtt_client):
    print("Start here")
   
    def on_message(client, userdata, msg):
        # print(msg)
        global all_msg, step
        message = decryptSV2UE(AESkey[0], msg.payload.decode())             # decrypted msg from mqtt
        print(f"Received data from `{msg.topic}` topic:", message)
        
        if check(message) != 0:                                              # merge msg
            step = check(message)
            print("step:", step)
            all_msg = ''
            # return True
        elif check(message) == 0:
            print("decrypted", step,": ",message)
            all_msg += message
            step -=1
            if step == 0:
                print("all_msg:",all_msg)
            # return True
            
   
    # client.subscribe(topic[1])
    if on_message == False:
        client.subscribe(topic[1])
        client.on_message = on_message
    else:
        client.subscribe(topic[1])
        client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()
    # subscribe(client)

if __name__ == '__main__':
    run()
