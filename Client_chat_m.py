import socket
import threading
import sys

# Configuración del cliente
HOST = '192.168.1.148'  # IP del servidor
PORT = 4443

# Crear un socket del cliente
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(message)
        except:
            # Si hay un error al recibir el mensaje, el servidor puede estar desconectado
            print('Error al recibir el mensaje. Saliendo.')
            client.close()
            sys.exit()

def send():
    name = input('Ingresa tu nombre: ')
    client.send(name.encode('utf-8'))
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()
    while True:
        message = input()
        if message.lower() == 'salir':
            client.send('salir'.encode('utf-8'))
            client.close()
            sys.exit()
        else:
            client.send(message.encode('utf-8'))

if __name__ == "__main__":
    send()
