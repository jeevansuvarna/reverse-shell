import socket
import sys


def create_socket():
    try:
        global host
        global port
        global soc
        host = ""
        port = 9999
        soc  = socket.socket()

    except socket.error as message:
        print("Error occured during socket creation "+str(message))

def bind_soc():
    try:
        global host
        global port
        global soc

        print("Binding the port "+str(port)+".......")
        soc.bind((host,port))
        soc.listen(5)
    except socket.error as message:
        print("Error occurred while binding!!"+str(message)+"Retrying ....")
        bind_soc()

def accept_socket():
    connection,address = soc.accept()
    print("Connection established!!! IP "+address[0]+" Port "+ str(address[1]))
    commandss(connection)
    connection.close()

def commandss(connection):
    while True:
        inp = input("Enter the command ")
        if inp == "quit":
            connection.close()
            soc.close()
            sys.exit()
        if len(str.encode(inp))>0:
            connection.send(str.encode(inp))
            output = str(connection.recv(1024),"utf-8")
            print(output,end="")
def main():
    create_socket()
    bind_soc()
    accept_socket()

main()


