import socket
import json
import sys


s = socket.socket()

port = 8080

s.connect(('192.168.114.6',port))


data = s.recv(1024)
data = data.decode('utf-8')


s.send(b'Thankyouuu from Client!');


dataJ = json.loads(data)

print(type(data))
print(data)

s.close()
