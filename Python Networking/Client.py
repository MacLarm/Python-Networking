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
    # Communication loop, exit when you type 'Bye'.
    while message.lower().strip() != 'bye':
        # Send the message
        client_socket.send(message.encode())
        # Retrieve the message that was sent back
        data = client_socket.recv(1024).decode()
        # Print the message
        print('Received from server: ' + data)
        # Get a new item.
        message = input(" -> ")
    # Close the socket when you are done.
    client_socket.close()

if __name__ == '__main__':
    client_program()
