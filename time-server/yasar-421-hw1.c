#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <time.h>

int main(int argc, char **argv){

	int port = atoi(argv[1]);

	int sockfd = socket(AF_INET, SOCK_STREAM, 0);
	struct sockaddr_in serverAddress;
	serverAddress.sin_family = AF_INET;
	serverAddress.sin_addr.s_addr = INADDR_ANY;
	serverAddress.sin_port = htons(port);

	bind(sockfd, (struct sockaddr*)&serverAddress, sizeof(serverAddress));

	listen(sockfd, 10);
  	
	int client_socket = accept(sockfd, NULL, NULL);
	time_t currentTime;
	time(&currentTime);
	printf("connected...\n");
	printf("It is %s", ctime(&currentTime));
	send(client_socket, ctime(&currentTime), 30, 0);
	printf("disconnected...\n");

return 0;

}

