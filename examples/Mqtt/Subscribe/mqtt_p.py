from microbit import *
from usocket import socket
import network

from umqttsimple import MQTTClient

#mqtt config
mqtt_server = '192.168.11.100'
client_id = 'wiz'
topic_pub = b'topic'
topic_msg = b'Hello I am microbit'

last_message = 0
message_interval = 5
counter = 0

#W5x00 chip init
def w5x00_init():
    nic = network.WIZNET5K() 
    nic.active(True)
    
    #None DHCP
    nic.ifconfig(('192.168.11.20','255.255.255.0','192.168.11.1','8.8.8.8'))
    print('IP address :', nic.ifconfig())
    
    while not nic.isconnected():
        sleep(1)
    
def mqtt_connect():
    client = MQTTClient(client_id, mqtt_server, keepalive=60)
    client.connect()
    print('Connected to %s MQTT Broker'%(mqtt_server))
    return client

def main():
    w5x00_init()
    
    client = mqtt_connect()

    while True:
        client.publish(topic_pub, topic_msg)
        sleep(1000)

    client.disconnect()

if __name__ == "__main__":
    main()