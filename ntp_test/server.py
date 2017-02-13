#!/usr/bin/python3

import time
import socketserver

get_time_us = lambda: str(round(time.time()*10**6))

class MyUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data_recvd_at = get_time_us()
#        data = self.request[0].strip()
        socket = self.request[1]
#        print("Time at client with IP {} :".format(self.client_address[0]))
#        print(data)
        data_sent_at = get_time_us()
        data = bytes(data_recvd_at  + "\n" + data_sent_at,"utf-8")
        socket.sendto(data, self.client_address)

HOST, PORT = "0.0.0.0", 9999
server = socketserver.UDPServer((HOST, PORT), MyUDPHandler)
server.serve_forever()
