#!/usr/bin/env python
import client

HOST = '::1'
PORT = 1111
BUFFER = 1024

if __name__ == '__main__':
    for i in range(1, 10000):
        client.set_key(str(i), str(i + 1))
        r = client.get_key(str(i))
        if (str(r) == str(i+1)):
            pass
        else:
            print str(i) + '=' + str(r) + ' error'
            exit(1)
    client.stop()

    exit(0)
