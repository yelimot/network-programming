import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 54545))

username = input("Choose your username: ")

# listening to server and sending username
def receive():
    while True:
        try:
            # receive message from the server
            # 'ID' means, username
            announcement = client.recv(1024).decode('utf8')
            if announcement == 'ID': # 'ID' is a keyword that implemented on server for getting usernames
                client.send(username.encode('utf8'))
            else: # anything except username means an announcement and printed
                print(announcement)
        except:
            # closig the connection when error occurs
            print("An error occured!")
            client.close()
            break

# sending announcements to the server
def write():
    while True:
        announcement = '{}: {}'.format(username, input(''))
        client.send(announcement.encode('utf8'))

# starting threads for multiprogramming
receive_thread = threading.Thread(target = receive)
receive_thread.start()

write_thread = threading.Thread(target = write)
write_thread.start()