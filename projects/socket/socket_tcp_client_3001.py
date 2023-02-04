import socket

SERVEUR_IP = 'localhost' # localhost si vide
SERVEUR_PORT = 3001
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Tentative de connexion au serveur {} port {}".format(SERVEUR_IP, SERVEUR_PORT))
sock.connect((SERVEUR_IP, SERVEUR_PORT))
print('Connecté au serveur')

try:
    while True:
        data = input('Données ?')
        if data == '':
            break
        sock.sendall(data.encode('utf-8'))      
        reponse = sock.recv(8192)
        print("Reçu (brute):" + str(reponse))
        print("Reçu (utf-8):" + reponse.decode('utf-8'))        
finally:    
    sock.close()

