# Overview

I wanted to learn some of the basics of programming networking. I wanted to use
python's socket library to learn more of the the methods and functions that are
availiable. 

[Software Demo Video](http://youtube.link.goes.here)

# Network Communication

The beta is a simple text messaging system. It uses a server to client architecture. 
The server grabs an availiable port then gives that to the user who can then give 
the port number to a client so that the two parties could chat. The client can exit
from the chat by typing 'bye'. 
By default the program uses the TCP protocol, it is not as fast but it is more secure.
Security is the higher priority as messages do not need much speed.

# Development Environment

This project was developed using VS code on Mac. 
I am using python version 3.10.11 with the standard python library 'socket'.
During testing I would run the server through the computer's terminal and the 
client from the terminal within VS code.
This should run on any computer with python installed.

# Useful Websites

* [socket — Low-level networking interface](https://docs.python.org/3/library/socket.html)
* [Transmission Control Protocol](https://en.wikipedia.org/wiki/Transmission_Control_Protocol)

# Future Work

Future Improvements.
* I want to make a single user interface, where you can choose between hosting a chat or joining one.
* I want to change the flow of the chat, to where you can send more than one message back to back
* I want to add options to share other types of data beside text.
