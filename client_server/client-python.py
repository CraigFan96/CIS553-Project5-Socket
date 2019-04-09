import sys
import socket

SEND_BUFFER_SIZE = 2048

'''
	Each client program should contact a server, 
	read a message from stdin, send the message, and exit.
	Each client should read and send the message exactly as 
	it appears in stdin until reaching an EOF (end-of-file).
	Each client should take two command-line arguments: the 
	IP address of the server and the port number of the server.
	Each client must be able to handle arbitrarily large messages 
	by iteratively reading and sending chunks of the message, 
	rather than reading the whole message into memory first.
	Each client should handle partial sends (when a socket only 
	transmits part of the data given in the last send call) by attempting 
	to re-send the rest of the data until it has all been sent.
	Each client should gracefully handle error values potentially 
	returned by socket programming library functions.
'''


def client(server_ip, server_port):
    """TODO: Open socket and send message from sys.stdin"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SEND_BUFFER_SIZE)
    s.connect((server_ip, server_port))
    data = s.recv(SEND_BUFFER_SIZE)
    print(sys.stdin)
    s.sendall('HELLO WORLD')
    for line in sys.stdin:

        total = len(line)
        begin = 0
        end = min(total, SEND_BUFFER_SIZE)
        while total > 0:
            print(line[begin:end])
            total -= end
            begin = end
            end = min(end + total, SEND_BUFFER_SIZE)
            s.send(line[begin:end])
    s.close()


def main():
    """Parse command-line arguments and call client function """
    if len(sys.argv) != 3:
        sys.exit("Usage: python client-python.py [Server IP] [Server Port] < [message]")
    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    print(sys.stdin)
    client(server_ip, server_port)


if __name__ == "__main__":
    main()
