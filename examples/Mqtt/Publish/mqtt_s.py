from microbit import *
from usocket import socket
import network

from umqttsimple import MQTTClient

#mqtt config
mqtt_server = '192.168.11.100'
client_id = 'wiz'
topic_sub = b'topic'

#W5x00 chip init
def w5x00_init():
    nic = network.WIZNET5K() 
    nic.active(True)
    
    nic.ifconfig(('192.168.11.20','255.255.255.0','192.168.11.1','8.8.8.8'))
    print('IP address :', nic.ifconfig())
    
    while not nic.isconnected():
        sleep(1)

def sub_cb(topic, msg):
    print((topic.decode('utf-8'), msg.decode('utf-8')))

def mqtt_connect():
    client = MQTTClient(client_id, mqtt_server, keepalive=60)
    client.set_callback(sub_cb)
    client.connect()
    print('Connected to %s MQTT Broker'%(mqtt_server))
    return client

def main():
    w5x00_init()
    
    client = mqtt_connect()

    while True:
        client.subscribe(topic_sub)

    client.disconnect()

if __name__ == "__main__":
    main()
