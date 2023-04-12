from socket import *
serverName = "127.0.0.1"
serverPort = 12000

#this creates the server's socket, 1st parameter indicates that the underlying network is using IPv4, 2nd parameter shows it is a TCP socket not UDP
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

#this line makes the server listen for TCP connection requests from the client. The parameter '1' specifies the max number of queued connections
serverSocket.listen(1)

#
print('The server is ready to receive')

#loop while true
while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence)
    connectionSocket.close()