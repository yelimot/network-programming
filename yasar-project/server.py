import threading
import socket

host = '127.0.0.1' # localhost
port = 54545

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creating server socket
server.bind((host, port)) # server is binding to the localhost on port '54545'
server.listen()

clients = [] # unique clients
usernames = [] # holds the usernames of clients

def announce(announcement):
    for client in clients:
        client.send(announcement)

# publishing announcements that came from clients
def publish(client):
    while True:
        try:
            # broadcasting annoucements
            announcement = client.recv(1024)
            announce(announcement) # if receiving successful, publish the announcement to everybody
        except:
            # Removing clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            announce('{} left!'.format(username).encode('utf8'))
            usernames.remove(username)
            break

# receiving / listening function
def receive():
    while True:
        # accepting the connection for client to the server
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # getting username from announcers
        client.send('ID'.encode('utf8'))
        username = client.recv(1024).decode('utf8')
        usernames.append(username)
        clients.append(client)

        # printing and publishing the username
        print("Username is {}".format(username))
        announce("{} joined!".format(username).encode('utf8'))
        client.send('Connected to the server succesfully!'.encode('utf8'))

        # one thread for each client
        thread = threading.Thread(target=publish, args=(client,))
        thread.start()

print("Server is listening...")
receive()
