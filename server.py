#!/usr/bin/env python
__author__ = 'rusik'
import socket

d = {}
IP = '::1'
PORT = 1111
BUFFER = 1024


def set_handler(key, value):
    print 'set_handler'
    d[key] = value
    print key + '=' + value
    return 'OK'


def get_handler(key):
    print 'get_handler'
    print key + '=' + d[key]
    return d[key]


if __name__ == '__main__':
    print 'starting'
    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    sock.bind((IP, PORT))
    sock.listen(1)
    while 1:
        conn, addr = sock.accept()
        data = conn.recv(BUFFER)
        action = data.split(' ')[0]
        if action == 'get':
            key = data.split(' ')[1]
            answer = get_handler(key)
            conn.send(answer)
        elif action == 'set':
            key = data.split(' ')[1]
            value = data.split(' ')[2]
            answer = set_handler(key, value)
            conn.send(answer)
        elif action == 'stop':
            conn.send('stopping')
            exit (0)
