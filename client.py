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

# Find the local host name attached to the computer running server.py - you will use this to connect on server.py
host_name = input(str(" Enter the hostname of the server"))

# Establish port connection
# 8080 is standard
# If code fails to run, open firewall settings and allow port 8080
# Allow both incoming and outgoing connections to port 8080
# X.connect is searching for a host name matching the input set on "host_name"
# If host name matches active host and port, connection will establish

port = 8080

x.connect((host_name, port))
print("Connected to chat server")

# Similar to server 'while' statement
# Allows incoming messages, decodes and displays them
# Allows response message, encodes and sends it

while 1:
    incoming_message = x.recv(1024)
    incoming_message = incoming_message.decode()
    print(" Server :", incoming_message)
    message = input(str(">>"))
    message = message.encode()
    x.send(message)
    print(" message has been sent...")
