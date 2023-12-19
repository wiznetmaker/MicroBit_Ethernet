
from microbit import *
from usocket import socket
import network

#W5x00 chip init
def w5x00_init():
    nic = network.WIZNET5K()
    print("here!!")
    nic.active(True)
    
    nic.ifconfig(('192.168.11.20','255.255.255.0','192.168.11.1','8.8.8.8'))
    print('IP address :', nic.ifconfig())
    
    while not nic.isconnected():
        sleep(1)        

def display_gesture(gesture_bytes):
    gesture_to_display = {
        "shake": Image.CONFUSED,
        "up": Image.ARROW_N,
        "down": Image.ARROW_S,  # Assuming you meant ARROW_S for "down"
        "face up": Image.HAPPY,
        "face down": Image.SAD,  # Assuming you meant SAD for "face down"
        "left": Image.ARROW_W,
        "right": Image.ARROW_E,
        "freefall": Image.SURPRISED,
        "3g": 3,
        "6g": 6,
        "8g": 8,  # Assuming you meant 8 for "8g"
    }
    
    # Decode the bytes to a string
    gesture = gesture_bytes.decode('utf-8').strip()

    # Check if the gesture is in the dictionary and display the corresponding image or number
    if gesture in gesture_to_display:
        display.show(gesture_to_display[gesture])
    else:
        print("Unknown gesture:", gesture)

# Example usage
# Suppose you received the byte message for "left"




def main():
    
    w5x00_init()
    s = socket()

    s.bind(('192.168.11.20', 5000)) #Motion_Detector IP
    s.listen(1)
    display.scroll('WAIT DEVICE')
    conn, addr = s.accept()
    print("Connect from:", addr) 
    display.show(Image.HEART)
    while True:    
        received_message = conn.recv(2048)
        print(received_message.decode('utf-8'))
        display_gesture(received_message)

if __name__ == "__main__":
    main()
