import sys
import socket

RECV_BUFFER_SIZE = 2048
QUEUE_LENGTH = 10
HOST = '127.0.0.1'
'''
Each server program should listen on a socket, wait for a client to connect,
receive a message from the client, print the message to stdout,
and then wait for the next client indefinitely.
Each server should take one command-line argument: the port number to
listen on for client connections.
Each server should accept and process client communications in an infinite
loop, allowing multiple clients to send messages to the same server.
The server should only exit in response to an external signal (e.g. SIGINT from pressing ctrl-c).
Each server should maintain a short (10) client queue and handle multiple client
connection attempts sequentially. In real applications, a TCP server would fork a new process to handle each client connection concurrently, but that is not necessary for this assignment.
Each server should gracefully handle error values potentially returned by socket
programming library functions (see specifics for each language below).
'''


def server(server_port):
    """TODO: Listen on socket and print received message to sys.stdout"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind((HOST, server_port))
    s.listen(QUEUE_LENGTH)
    conn, addr = s.accept()
    print("Initiating server")
    while True:
        data = conn.recv(RECV_BUFFER_SIZE)
        print(data)
    conn.close()


def main():
    """Parse command-line argument and call server function """
    if len(sys.argv) != 2:
        sys.exit("Usage: python server-python.py [Server Port]")
    server_port = int(sys.argv[1])
    server(server_port)


if __name__ == "__main__":
    main()
