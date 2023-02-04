#!/bin/python
# -*- coding: utf-8 -*-

import socket

SERVEUR_IP = 'localhost' # localhost si vide
SERVEUR_PORT = 3000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Client echo en UDP port " + str(SERVEUR_PORT))
try:
    while True:
        data = input('Données ?')
        if data == '':
            break
        sock.sendto(data.encode('utf-8'), (SERVEUR_IP, SERVEUR_PORT))
        #https://docs.python.org/3/library/socket.html#socket.socket.recvfrom
        (reponse, (serveur_ip, serveur_port)) = sock.recvfrom(8192)
        print("Reçu (brute):" + str(reponse))
        print("Reçu (utf-8):" + reponse.decode('utf-8'))        
finally:
    sock.close()
