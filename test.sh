#!/usr/bin/env bash
set -x
./client.py set 1 2
./client.py get 1
./client.py blahblah
./client.py stop