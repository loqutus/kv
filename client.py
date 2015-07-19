#!/usr/bin/env python
__author__ = 'rusik'

import socket
import sys

HOST = '::1'
PORT = 1111
BUFFER = 1024


def get_key(key):
    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    sock.send('get ' + key)
    value = sock.recv(BUFFER)
    sock.close()
    return value


def set_key(key, value):
    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    sock.send('set ' + key + ' ' + value)
    sock.close()
    return value


def stop():
    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    sock.send('stop')
    sock.close()


if __name__ == '__main__':
    action = sys.argv[1]
    if action == 'get':
        key = sys.argv[2]
        print key + '=' + get_key(sys.argv[2])
    elif action == 'set':
        key = sys.argv[2]
        value = sys.argv[3]
        print key + '=' + set_key(key, value)
    elif action == 'stop':
        stop()
    else:
        print 'error action, exiting'
        exit(0)
    exit(0)
