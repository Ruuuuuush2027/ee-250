# team members: Junsoo Kim, Mo Jiang
# link: https://github.com/Ruuuuuush2027/ee-250.git
import paho.mqtt.client as mqtt
import time

"""This function (or "callback") will be executed when this client receives 
a connection acknowledgement packet response from the server. """
def on_connect(client, userdata, flags, rc):
    print("Connected to RPi broker with result code "+str(rc))
    #subscribe to pong topic
    client.subscribe("junsooki/pong")
    #add custom callback for pong
    client.message_callback_add("junsooki/pong", on_message_from_pong)

def on_message(client, userdata, msg):
    print("Default callback - topic: " + msg.topic + "   msg: " + str(msg.payload, "utf-8"))

#Custom callback for pong messages
def on_message_from_pong(client, userdata, message):
    received_number = int(message.payload.decode())
    print("Received pong: " + str(received_number))
    new_number = received_number + 1
    time.sleep(1)
    print("Publishing ping: " + str(new_number))
    client.publish("junsooki/ping", new_number)


if __name__ == '__main__':

    #create a client object
    client = mqtt.Client()
    #attach a default callback for incoming mqtt messages
    client.on_message = on_message
    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect

    #connect to RPi broker
    client.connect(host="172.20.10.13", port=1883, keepalive=60)

    client.loop_start()
    time.sleep(2)

    #publish initial number to start the chain
    print("Publishing initial ping: 1")
    client.publish("junsooki/ping", 1)


    while True:
        time.sleep(1)