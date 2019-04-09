import sys
import socket

RECV_BUFFER_SIZE = 2048
QUEUE_LENGTH = 10


def server(server_port):
    """TODO: Listen on socket and print received message to sys.stdout"""
    """
    Listen on a socket and wait for client to connect
    Once a message is received, print the message to stdout. Then wait for the next client (loop)
    Maintain a short client queue to handle multiple attempts sequentially
    Handle error values returned by socket programming library -> no additional error handling is required
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", server_port))
    s.listen(QUEUE_LENGTH)
    while 1:
        conn, addr = s.accept()
        data = conn.recv(RECV_BUFFER_SIZE)
        while data:
            sys.stdout.write(data)
            data = conn.recv(RECV_BUFFER_SIZE)
        sys.stdout.flush()

    conn.close()


def main():
    """Parse command-line argument and call server function """
    if len(sys.argv) != 2:
        sys.exit("Usage: python server-python.py [Server Port]")
    server_port = int(sys.argv[1])
    server(server_port)


if __name__ == "__main__":
    main()
