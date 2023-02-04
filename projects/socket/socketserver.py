import socketserver


SERVEUR_IP = '' # localhost si vide
SERVEUR_PORT = 3001

class GestionnaireEcho(socketserver.BaseRequestHandler):
    def handle(self):
        print('Connexion de ', self.client_address)
        while True:
            data = self.request.recv(8192)
            if not data : break
            print(data)
            self.request.sendall(data)
        self.request.close()
        print('Déconnexion de ', self.client_address)
        
serveur = socketserver.TCPServer((SERVEUR_IP, SERVEUR_PORT), GestionnaireEcho)
serveur.serve_forever()
