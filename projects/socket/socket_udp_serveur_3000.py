#!/bin/python
# -*- coding: utf-8 -*-

import socket

SERVEUR_IP = '' # localhost si vide
SERVEUR_PORT = 3000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVEUR_IP, SERVEUR_PORT)) #Création du socket

print("Serveur echo en UDP port " + str(SERVEUR_PORT))
print(' - '*8)
print('Attente de client...(Quitter avec Ctrl-C)')
try:
    while True:
        #https://docs.python.org/3/library/socket.html#socket.socket.recvfrom
        (data, (client_ip, client_port)) = sock.recvfrom(8192)
        print("- Datagramme depuis " , end="")
        print(client_ip, end="")
        print(' port ' + str(client_port))
        print(" - brute:" + str(data))
        print(" - utf-8:" + data.decode('utf-8'))
        sock.sendto(data, (client_ip, client_port))
        
finally:
    sock.close()

