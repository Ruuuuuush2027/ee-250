# Lab 2

## Team Members
- Mo Jiang
- Junsoo Kim

## Lab Question Answers

Answer for Question 1: 
* argc is the number of arguments parsed in when calling the executable of this C
* argv is a list of char arrays that point to specific input parameters

Answer for Question 2: 
*  A file descriptor is a positive integer identifying a file and I/O source (like socket).
*  The file descriptor table is a structure for each process that maps integers to file descriptionsso the files can be opened based on file des criptor

Answer for Question 3:
* A struct is a grouping variables of different types.
* sockaddr_in is a struct defined in netinet/in.h for IPv4 internet addresses, containing info like address family, port number, IP address, etc.

Answer for Question 4:
* communication domain (AF_INET = IPv4 protocol), socket type(SOCK_STREAM is for TCP), and protocol (0 is automatically chosen by system)

Answer for Question 5:
* bind(): the socket file descriptor, a pointer to the address structure (containing IP/port), and the size of that address structure.
* listen(): the socket file descriptor and the maximum number of pending connections one can have.

Answer for Question 6:
* while(1) because we want server always open to new connections, so server won't just shutdown automatucally
* no new threads are created, so server can only deal with one connection at a time and clients will be waiting for each other

Answer for Question 7:
* fork() basically copies the current program and starts a new child process to continue executing same code
* for each new connection established, one can call fork() to fork() a child process. If it's a child process execute the handling code and shutdown. Otherwise continue looping as server main loop.

Answer for Question 8:
* A syscall is a request sent by the program to the kernel for functions program itself doesn't have access to, such as reading and opening files, which need to be handled by kernel