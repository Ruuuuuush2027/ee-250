# team members: Junsoo Kim, Mo Jiang
# link: https://github.com/Ruuuuuush2027/ee-250.git
import paho.mqtt.client as mqtt
import time

"""This function (or "callback") will be executed when this client receives 
a connection acknowledgement packet response from the server. """
def on_connect(client, userdata, flags, rc):
    print("Connected to RPi broker with result code "+str(rc))
    #subscribe to ping topic
    client.subscribe("junsooki/ping")
    #add custom callback for ping
    client.message_callback_add("junsooki/ping", on_message_from_ping)

def on_message(client, userdata, msg):
    print("Default callback - topic: " + msg.topic + "   msg: " + str(msg.payload, "utf-8"))

#Custom callback for ping messages
def on_message_from_ping(client, userdata, message):
    received_number = int(message.payload.decode())
    print("Received ping: " + str(received_number))
    new_number = received_number + 1
    time.sleep(1)
    print("Publishing pong: " + str(new_number))
    client.publish("junsooki/pong", new_number)


if __name__ == '__main__':

    #create a client object
    client = mqtt.Client()
    #attach a default callback for incoming mqtt messages
    client.on_message = on_message
    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect

    #connect to RPi broker
    client.connect(host="172.20.10.13", port=1883, keepalive=60)

    print("Waiting for ping messages...")
    client.loop_forever()