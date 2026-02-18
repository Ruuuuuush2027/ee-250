/* A simple server in the internet domain using TCP
 * Answer the questions below in your writeup
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h> 
#include <sys/socket.h>
#include <netinet/in.h>

void error(const char *msg)
{
    perror(msg);
    exit(1);
}

int main(int argc, char *argv[])
{
    /* 1. What is argc and *argv[]?
     * argc is the number of arguments parsed in when calling the executable of this C
     * argv is a list of char arrays that point to specific input parameters
     */
    int sockfd, newsockfd, portno;
    /* 2. What is a UNIX file descriptor and file descriptor table?
     *  A file descriptor is a positive integer identifying a file and I/O source (like socket).
     *  The file descriptor table is a structure for each process that maps integers to file descriptions
     *  so the files can be opened based on file descriptor
     */
    socklen_t clilen;

    struct sockaddr_in serv_addr, cli_addr;
    /* 3. What is a struct? What's the structure of sockaddr_in?
     * A struct is a grouping variables of different types.
     * sockaddr_in is a struct defined in netinet/in.h for IPv4 internet addresses, 
     * containing info like address family, port number, IP address, etc.
     */
    
    int n;
    if (argc < 2) {
        fprintf(stderr,"ERROR, no port provided\n");
        exit(1);
    }
    
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    /* 4. What are the input parameters and return value of socket()
     * communication domain (AF_INET = IPv4 protocol), socket type(SOCK_STREAM is for TCP), 
     * and protocol (0 is automatically chosen by system)
     */
    
    if (sockfd < 0) 
       error("ERROR opening socket");
    bzero((char *) &serv_addr, sizeof(serv_addr));
    portno = atoi(argv[1]);
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_addr.s_addr = INADDR_ANY;
    serv_addr.sin_port = htons(portno);
    
    if (bind(sockfd, (struct sockaddr *) &serv_addr,
             sizeof(serv_addr)) < 0) 
             error("ERROR on binding");
    /* 5. What are the input parameters of bind() and listen()?
     * bind(): the socket file descriptor, a pointer to the address structure (containing IP/port),
     * and the size of that address structure.
     * listen(): the socket file descriptor and the maximum number of pending connections one can have.
     */
    
    listen(sockfd,5);
    clilen = sizeof(cli_addr);
    
    while(1) {
        /* 6.  Why use while(1)? Based on the code below, what problems might occur if there are multiple simultaneous connections to handle?
        * while(1) because we want server always open to new connections, so server won't just shutdown automatucally
        * no new threads are created, so server can only deal with one connection at a time and clients will be waiting for each other
        */
        
	char buffer[256];
        newsockfd = accept(sockfd, 
                    (struct sockaddr *) &cli_addr, 
                    &clilen);
	/* 7. Research how the command fork() works. How can it be applied here to better handle multiple connections?
         * fork() basically copies the current program and starts a new child process to continue executing same code
         * for each new connection established, one can call fork() to fork() a child process. If it's a child process 
         * execute the handling code and shutdown. Otherwise continue looping as server main loop.
         */
        
	if (newsockfd < 0) 
             error("ERROR on accept");
	bzero(buffer,256);
        
	    n = read(newsockfd,buffer,255);
        if (n < 0) 
            error("ERROR reading from socket");
        printf("Here is the message: %s\n",buffer);
        n = write(newsockfd,"I got your message",18);
        if (n < 0) 
            error("ERROR writing to socket");
        close(newsockfd);
    }
    close(sockfd);
    return 0; 
}
  
/* This program makes several system calls such as 'bind', and 'listen.' What exactly is a system call?
 *
 */