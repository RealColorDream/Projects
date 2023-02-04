import socket

SERVEUR_IP = '' # localhost si vide
SERVEUR_PORT = 3001
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((SERVEUR_IP, SERVEUR_PORT)) #Création du socket
sock.listen(5)

print("Serveur echo en TCP port " + str(SERVEUR_PORT))
print(' - '*8)
print('Attente de client...(Quitter avec Ctrl-C)')
try:
    while True:
        (new_socket, (client_ip, client_port)) = sock.accept()
        print("- Connexion client depuis " , end="")
        print(client_ip, end="")
        print(' port ' + str(client_port))
        while True:
            data = new_socket.recv(8192)
            if not data:
                break
            print("  Reçu (brute):{}".format(data))            
            print("  Reçu (utf-8):{}".format(data.decode('utf-8')))
            new_socket.sendall(data)
        new_socket.close()
        print(" Déconnexion de {}:{}".format(client_ip, client_port))
finally:
    sock.close()
