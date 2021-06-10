import socket
import os
import time

#create socket
s = socket.socket()


port = 8880

#connect to server
s.connect(('192.168.114.6',port))

#File to be sent
file_name = input("[+]File name:")
file_size = os.path.getsize(file_name)

#Send file to server
s.send(file_name.encode())
s.send(str(file_size).encode())

# Open and read file
with open(file_name,"rb") as file:

	c = 0

	#Start time record
	start_time = time.time()

	#loop for sent the file
	while c <= file_size:
		data1 = file.read(1024)
		if not (data1):
			break
		s.sendall(data1)
		c = c + len(data1)

	#end time record
	end_time = time.time()


print("[+] File transfer to server complete! Total time: ",end_time - start_time)

#close socket
s.close() 

s.close()
