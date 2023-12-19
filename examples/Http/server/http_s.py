from microbit import *
import network
import socket

def w5x00_init():
    nic = network.WIZNET5K() 
    nic.active(True)
    
    #None DHCP
    nic.ifconfig(('192.168.11.20','255.255.255.0','192.168.11.1','8.8.8.8'))
    print('IP address :', nic.ifconfig())
    
    while not nic.isconnected():
        sleep(1)

def http_server():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(5)

    while True:
        print("Wait client ...")        
        cl, addr = s.accept()
        print("Connect from:", addr)
        
        cl_file = cl.makefile('rwb', 0)
        while True:
            line = cl_file.readline()
            if not line or line == b'\r\n':
                break
    
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send('<html><body><h1>Hello, World!</h1></body></html>\r\n')
        cl.close()
        
def main():
    w5x00_init()
    http_server()

if __name__ == "__main__":
    main()        
