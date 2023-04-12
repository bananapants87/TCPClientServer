from socket import *
serverName = '127.0.0.1' 
serverPort = 12000

#this creates the client's socket, 1st parameter indicates that the underlying network is using IPv4, 2nd parameter shows it is a TCP socket not UDP
clientSocket = socket(AF_INET, SOCK_STREAM) 


#this initiates the TCP connection between the client and server
clientSocket.connect((serverName, serverPort))

#this gets a sentence from the user
sentence = input('Input lowercase sentence: ')

#this sends the sentence through the client's socket and into the TCP connection
clientSocket.send(bytes(sentence, "ascii"))

#this places the characters that arrived from the server into the variable 'modifiedSentence'
modifiedSentence = clientSocket.recv(1024)

#This displays the modified sentence to the user
print ('From server: ', modifiedSentence)

#this line closes the socket and TCP connection between the client and the server
clientSocket.close()

