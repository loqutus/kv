#!/usr/bin/env python
__author__ = 'rusik'
import socket
import time
from logging import debug
import logging

d = {}
lock = []
IP = '::1'
PORT = 1111
BUFFER = 1024

logging.basicConfig(filename='server.log',
                    format=u'[LINE:%(lineno)d]#[%(asctime)s]  %(message)s',
                    level=logging.DEBUG)
log = logging.getLogger(__name__)


def set_handler(key, value):
    debug('set_handler')
    while key in lock:
        debug('set lock wait')
        time.sleep(0.1)
    lock.append(key)
    d[key] = value
    lock.remove(key)
    return 'OK'


def get_handler(key):
    debug('get_handler')
    while key in lock:
        debug('get lock wait')
        time.sleep(0.1)
    debug('get lock append')
    lock.append(key)
    ret = d[key]
    lock.remove(key)
    return ret

if __name__ == '__main__':
    debug('starting')
    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((IP, PORT))
    sock.listen(1)
    while 1:
        debug('while')
        conn, addr = sock.accept()
        data = conn.recv(BUFFER)
        action = data.split(' ')[0]
        if action == 'get':
            debug('get')
            key = data.split(' ')[1]
            answer = get_handler(key)
            conn.send(answer)
            debug('get answer send')
        elif action == 'set':
            debug('set')
            key = data.split(' ')[1]
            value = data.split(' ')[2]
            answer = set_handler(key, value)
            conn.send(answer)
            debug('set answer send')
        elif action == 'stop':
            conn.send('stopping')
            sock.close()
            debug('stopping')
            exit(0)
