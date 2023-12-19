from microbit import *
from usocket import socket
import network

import urequests

def w5x00_init():
    nic = network.WIZNET5K() 
    nic.active(True)
    
    #None DHCP
    nic.ifconfig(('192.168.11.20','255.255.255.0','192.168.11.1','8.8.8.8'))
    print('IP address :', nic.ifconfig())
    
    while not nic.isconnected():
        sleep(1)
        
def request():
    r = urequests.get('http://httpbin.org/get')
    #r.raise_for_status
    print(r.status_code)
    print(r.text)


def main():
    w5x00_init()
    request()

if __name__ == "__main__":
    main()