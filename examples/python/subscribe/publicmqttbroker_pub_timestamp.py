# mqtt timestamp subscribe example

import paho.mqtt.client as paho
import time

broker = "publicmqttbroker.iiotmq.com"  # https://publicmqttbroker.iiotmq.com/
port = 1883


def on_publish(client, userdata, result):
    print("data published")


client = paho.Client("publicmqttbroker_testtopic_pub")
client.username_pw_set("publicmqttbroker", "publicmqttbroker")
client.on_publish = on_publish
client.connect(broker, port)

for i in range(10):
    t = int(time.time())
    ret = client.publish("timestamp", "%s" % t)  # publish
    time.sleep(1)
