# Part of python's standard libaray, it allows us to manage network connections
# using sockets. 
import socket

'''
server_program
Inputs: None.
Outputs: None.
This function sets up the needed sockets for a host to connect to a peer and 
allow for simple chat to take place between them.
'''
def server_program():
    NUM_CONNECTIONS = 2


    # Saves the name of the machine running the server program.
    host = socket.gethostname()

    # Create a server object with default paramaters
    server_socket = socket.socket() # Create a TCP socket

    # Here we bind the host to socket object and an availiable port.
    # This lets the machine listen for connections.
    server_socket.bind((host, 0)) 

    # Get the name of the port so we can be able to share it with any clients.
    port = server_socket.getsockname()[1] # sockname is retuned as a touple: (host, port), we want port.
    print(f"Assigned port: {port}") # Print the port number.

    # Start listening for connections
    server_socket.listen(NUM_CONNECTIONS) # Don't let any more than NUM_CONNECTIONS enter.

    # Wait until the connection is made and pass the socket and address back.
    conn, address = server_socket.accept()
    print("Connection from: " + str(address)) # Print the connection.

    done = False # Sentinal variable for our loop.

    while not done: # Run until we meet an exit condition.
        incoming_message = conn.recv(1024).decode() # Decode the the message (up to 1024 bytes).
        if not incoming_message: # Check if a messafe was recieved.
            done = True # If nothing was recieved we exit the loop.
        print("From connected user: " + str(incoming_message)) # Print the recieved message.
        response = input(' -> ') # Prompt the client to respond.
        conn.send(response.encode()) # Send the message back
    conn.close() # Close the connection

if __name__ == '__main__':
    server_program()
