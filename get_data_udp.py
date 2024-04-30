import socket
from struct import *
UDP_IP = "127.0.0.1"
UDP_PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(5000)
    print("Received data:", data)
    p_data = unpack("<if1024i",data);
    print(p_data)
