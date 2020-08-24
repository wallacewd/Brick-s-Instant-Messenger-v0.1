"""
Basic Instant Messaging Application Version 0.1
Author: Dan Wallace (danwallaceasu@gmail.com).
Creates a peer to peer connection on a local network allowing real-time chat.
Server.py must be running in order for both files to run.
Server.py creates a server that is only active when the code is running.
08/23/2020
"""

# Import socket is needed to interface with ports

import socket
import sys
import time

# Attaches socket (must have socket imported to do this) to variable so we can use rapidly
x = socket.socket()

# Find the local host name attached to the computer running server.py - you will use this to connect on client.py

host_name = socket.gethostname()
print("server will start on host: ", host_name)

# Establish port connection
# 8080 is standard
# If code fails to run, open firewall settings and allow port 8080
# Allow both incoming and outgoing connections to port 8080
# X.bind is binding the host name and port to the python socket function.

port = 8080
x.bind((host_name, port))
print("server done binding to host and port successfully")
print("server is waiting for incoming connections")

# Asks to the socket to listen for incoming connections, limited to 1 connection

x.listen(1)

# connection and address are accepted to the socket (for more info: look up python sockets)

connection, address = x.accept()

print(address, " Has connected to the server and is now online...")

# While the user is connected (1 because we only allow 1 extra connection)
# Creates input field for chat message and attached to variable
# Chat message input is converted to bytes in order to send
# Another variable is created to allow incoming messages and decodes it from bytes
# Connection.recv is set to port 1024..still working out why this is, i just know this works haha

while 1:
   display_message= input(str(">>"))
   display_message= display_message.encode()
   connection.send(display_message)
   print(" message has been sent...")
   inMessage= connection.recv(1024)
   inMessage= inMessage.decode()
   print(" Client:", inMessage)
