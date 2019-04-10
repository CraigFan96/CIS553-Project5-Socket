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

#define QUEUE_LENGTH 10
#define RECV_BUFFER_SIZE 2048

/* TODO: server()
 * Open socket and wait for client to connect
 * Print received message to stdout
 * Return 0 on success, non-zero on failure
*/
int server(char *server_port) {
	int s, client_length, c, n;
	struct sockaddr_in serv_addr;
	struct sockaddr_in client_addr;
	char buf[RECV_BUFFER_SIZE];

	serv_addr.sin_family = AF_INET;
  	serv_addr.sin_addr.s_addr = INADDR_ANY;
  	serv_addr.sin_port = htons(atoi(server_port));

    s = socket(AF_INET, SOCK_STREAM, 0);
    if (s < 0) {
    	perror("ERROR opening socket");
    	exit(1);
	}

	if (bind(s, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0 ) {
		perror("ERROR on bind");
		exit(1);
	}

	if (listen(s, QUEUE_LENGTH) < 0) {
		perror("ERROR listening");
		exit(1);
	}

	client_length = sizeof(client_addr);

	while (1) {
		c = accept(s, (struct sockaddr * ) &client_addr, &client_length);
		if (c < 0) {
			perror("ERROR on accept");
		}

		bzero(buf, RECV_BUFFER_SIZE);
		n = read(c, buf, RECV_BUFFER_SIZE);
		if (n < 0) {
			perror("ERROR reading socket");
		} else {
			printf("%s", buf);
		}
		fflush(stdout);
	}

}

/*
 * main():
 * Parse command-line arguments and call server function
*/
int main(int argc, char **argv) {
  char *server_port;

  if (argc != 2) {
    fprintf(stderr, "Usage: ./server-c [server port]\n");
    exit(EXIT_FAILURE);
  }

  server_port = argv[1];
  return server(server_port);
}
