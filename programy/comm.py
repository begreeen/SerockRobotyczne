import sys
import time
import os
import socket
import sys


class Communication:
    def __init__(self, address, port):
        self.comm = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (address, port)
        self.start_time = time.time()

        try:
            print('Connecting...')
            self.comm.connect(server_address)
        except:
            print('Could not connect to server.')
            sys.exit()

    def send(self, data, name):
        t = time.time() - self.start_time
        str_data = '{};{};{}\r\n'.format(name, t, data)
        self.comm.sendall(str_data.encode('utf-8'))

    def close(self):
        self.comm.close()
