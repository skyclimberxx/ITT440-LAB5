import socket 
import sys
import json

mydata = {"ID":505012, "Name": "Azizi", "Age": "29"}
sendData = json.dumps(mydata)


# create socket
s = socket.socket()
print("[+] Socket succesfully created!")


port = 8080

#bind socket
s.bind(('',port))
print("[+] Socket binded to: "+ str(port))

#listen client
s.listen(5)
print("[+] Sokcet is listening to connection...")

while True:

	c, addr = s.accept()
	print("[+] Fot connection from: "+ str(addr))

	c.sendall(bytes(sendData,encoding='utf-8'))
	buffer = c.recv(1024)
	print(buffer)


c.close()
