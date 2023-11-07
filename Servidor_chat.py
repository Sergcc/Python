#Programa Ejercicio 7 SCC Octubre 2013 Servidor Listener Chat

import socket
import threading

# Configuración del servidor
host = "192.168.1.148"  # Cambia la dirección IP del servidor
port = 4443

# Lista de clientes conectados
clients = []

# Función para manejar las conexiones de los clientes
def handle_client(client_socket, client_address):
    name = "usuario" + str(len(clients))
    print(f"Conexión aceptada de {client_address}. Ahora eres {name}.")
    client_socket.send(f"Bienvenido, eres {name}.".encode())

    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                print(f"{name} ha terminado la sesión.")
                clients.remove((client_socket, name))
                client_socket.close()
                break

            message = message.decode()
            print(f"{name}: {message}")

            # Reenviar el mensaje a todos los clientes
            for client, _ in clients:
                if client != client_socket:
                    client.send(f"{name}: {message}".encode())
        except:
            print(f"{name} ha tenido un error.")
            clients.remove((client_socket, name))
            client_socket.close()
            break

# Configuración del servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(10)
print(f"Servidor escuchando en {host}:{port}")

# Aceptar conexiones entrantes
while True:
    client_socket, client_address = server.accept()
    clients.append((client_socket, "usuario" + str(len(clients)))
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
