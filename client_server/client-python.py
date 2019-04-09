import sys
import socket

SEND_BUFFER_SIZE = 2048


def client(server_ip, server_port):
    """TODO: Open socket and send message from sys.stdin"""
    """
    Contact server
    Read message from stdin and send message (exactly as read) and exit
    handle arbitrarily large messages by iteratively read and sending chunks (not read whole message)
    handle partial sends by re-sending rest of data
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))

    with sys.stdin as f:
        data = f.read(SEND_BUFFER_SIZE)
        while data:
            s.send(data)
            data = f.read(SEND_BUFFER_SIZE)

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
