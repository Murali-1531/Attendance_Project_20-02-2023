import socket
s=socket.socket((socket.AF_INET,socket.SOCK_STREAM))
s.listen(10)
while True:
	c,addr=S,accept()
	c.send("hi Priya".encode())
	data=c.recv(1024)
	print(data)
	if(data=="bye"):
		break
