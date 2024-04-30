import socket
from struct import *

import numpy as np
UDP_IP = "127.0.0.1"
UDP_PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(5000)
    #    print("Received data:", data)
    p_data = unpack("<if1024i",data);
    a = p_data[0]
    b = p_data[1]
    sin_m = p_data[2:]
    print("\n sizeof = ",data.__sizeof__())
    size_mass = len(sin_m)
    print("\n size mass = ",size_mass)
    count = np.linspace(0,1,size_mass)
    print("\n count =",count)
    print(f"a: {a}  b:{b},mass={sin_m}")

