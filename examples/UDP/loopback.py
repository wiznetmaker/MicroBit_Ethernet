from microbit import *
import socket
import network

#W5x00 chip init
def w5x00_init():
    nic = network.WIZNET5K() 
    nic.active(True)
    
    nic.ifconfig(('192.168.11.20','255.255.255.0','192.168.11.1','8.8.8.8'))
    print('IP address :', nic.ifconfig())
    
    while not nic.isconnected():
        sleep(1)

def loopback ():
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('0.0.0.0', 5000))

    print("Loopback start")
    while True:
        data, addr = s.recvfrom(1024)
        print("Received message:", data, addr)

        if data != 'NULL':
            s.sendto(data, addr)

    

def main():
    w5x00_init()
    loopback()

if __name__ == "__main__":
    main()
