#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netdb.h>
#include <netinet/in.h>
#include <errno.h>

#define SEND_BUFFER_SIZE 2048
#define SA struct sockaddr


/* TODO: client()
 * Open socket and send message from stdin.
 * Return 0 on success, non-zero on failure
*/
int client(char *server_ip, char *server_port) {
  int s, rcode;
  char input[SEND_BUFFER_SIZE];
  int bytes_sent, len;
  struct sockaddr_in servaddr;
  // create and verify socket
  s = socket(AF_INET, SOCK_STREAM, 0);
  if (s < 0) {
      printf("Socket creation failure");
      exit(1);
   }
  // assign IP, PORT
  servaddr.sin_family = AF_INET;
  servaddr.sin_addr.s_addr = inet_addr(server_ip);
  servaddr.sin_port = htons(atoi(server_port));

  // connect the client socket to server socket
  rcode = connect(s, (SA*)&servaddr, sizeof(servaddr));
  if (rcode < 0) {
    printf("Connection with server failed\n");
    exit(0);
  } else {
    printf("Connected to the server\n");
    while (fgets (input, SEND_BUFFER_SIZE, stdin)) {
      len = strlen(input);
      bytes_sent = send(s, input, len, 0);
    }
  }
  close(s);
  return 0;
}

/*
 * main()
 * Parse command-line arguments and call client function
*/
int main(int argc, char **argv) {
  char *server_ip;
  char *server_port;

  if (argc != 3) {
    fprintf(stderr, "Usage: ./client-c [server IP] [server port] < [message]\n");
    exit(EXIT_FAILURE);
  }

  server_ip = argv[1];
  server_port = argv[2];
  return client(server_ip, server_port);
}
