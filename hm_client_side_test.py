import socket

# import threading

PORT = 5050
IPv4 = "26.253.46.146"
ADDR = (IPv4, PORT)
FORMAT = 'utf-8'
HEADER = 64

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    
def recieve():
    msg_length = client.recv(HEADER).decode(FORMAT)
    msg = ""
    if msg_length:
        msg_length = int(msg_length)
        msg = client.recv(msg_length).decode(FORMAT)
    return msg

def load():
    msg = ""
    while msg != "s":
        msg = recieve()
        if msg != "s":
            print(msg)
def method_w():
    print("Pick a word for the guesser:", end = "")
    word = input()
    send(word)
   
def method_c():
    print(recieve(), end = "")
    letter = input()
    while len(letter)>1:
        letter= input('I said a letter (no whitespace):')
    send(letter)

def method_p():
    print(recieve())
    
def game_init():
    load()
    while True:
        method = recieve()
        method = "method_"+method+"()"
        try:
         eval(method)
        except:
            print("this is the exit screen")
            break
        
game_init()
print("welp if this line is printed then i guess the game worked?" "---- it is indeed worked :D")