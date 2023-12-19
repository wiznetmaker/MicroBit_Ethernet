
from microbit import *
from usocket import socket
import network

current_status = None
previous_status = None

#W5x00 chip init
def w5x00_init():
    nic = network.WIZNET5K()
    print("here!!")
    nic.active(True)
    
    nic.ifconfig(('192.168.11.120','255.255.255.0','192.168.11.1','8.8.8.8'))
    print('IP address :', nic.ifconfig())
    
    while not nic.isconnected():
        sleep(1)
        
def update_status():
    global current_status, previous_status

    gestures = ["shake", "up", "down", "face up", "face down", "left", "right", "freefall", "3g", "6g", "8g"]

    for gesture in gestures:
        try:
            if accelerometer.is_gesture(gesture):
                current_status = gesture
                break
        except ValueError:
            print("Invalid gesture:", gesture)

    if current_status != previous_status:
        #print(current_status)
        previous_status = current_status
        return True
    return False

def main():
    w5x00_init()
    s = socket()

    s.connect(('192.168.11.20', 5000)) #Display Device IP Address
    while True:
        if update_status():
            print("send", current_status.encode('utf-8'))
            data= current_status.encode('utf-8') + b'\n'
            s.send(data)
        
if __name__ == "__main__":
    main()
