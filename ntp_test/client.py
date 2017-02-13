#!/usr/bin/python3

import time
import sys
import socket

get_time_us = lambda: str(round(time.time()*10**6))

HOST, PORT = sys.argv[1], 9999
data = get_time_us()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes(data + "\n", "utf-8"), (HOST, PORT))
data_sent_at = get_time_us()

received = sock.recv(1024)
data_recvd_at = get_time_us()
received = str(received,"utf-8").split("\n")

print("Client : {} {}".format(data_sent_at,data_recvd_at))
print("Server: {} {}".format(received[0],received[1]))
latency_us = str(int(data_recvd_at) - int(data_sent_at))
print("latency = "+ latency_us + " us")
