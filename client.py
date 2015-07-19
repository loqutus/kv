#!/usr/bin/env python
__author__ = 'rusik'

import socket
import sys

HOST = '::1'
PORT = 1111
BUFFER = 1024


def get_key(key):
    print 'get_key ' + key
    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    sock.send('get ' + key)
    print sock.recv(BUFFER)
    return key


def set_key(key, value):
    print 'set_key ' + key + ' ' + value
    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    sock.send('set ' + key + ' ' + value)
    print sock.recv(BUFFER)
    return 0

def stop():
    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    sock.send('stop')


if __name__ == '__main__':
    if sys.argv[1] == 'get':
        get_key(sys.argv[2])
    elif sys.argv[1] == 'set':
        set_key(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'stop':
        stop()
    else:
        print 'error action, exiting'
        exit(0)
    exit(0)
