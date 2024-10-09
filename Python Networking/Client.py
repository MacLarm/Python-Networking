import socket

def client_program():
    # Set up the host/port touple to connect to the socket.
    host = socket.gethostname()
    port = int(input("Enter the Server's host number."))
    # create socket object with default settings, then connect to the host.
    client_socket = socket.socket()
    client_socket.connect((host, port))

    print("Welcome to the chat!")
    # Input for message.
    message = input(" -> ")
    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()

        print('Received from server: ' + data)

        message = input(" -> ")

    client_socket.close()

if __name__ == '__main__':
    client_program()
