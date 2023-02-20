a=int(input("Enter The  A Value:"))
b=int(input("Enter The  B Value:"))
print("(+)--> ADD (-)--> SUB (*)--> MUL (/)--> DIV (%)--> MOD ")
ch=input("Enter The Choice:")
if(ch=="+"):
	print(a+b)
elif(ch=="-"):
	print(a-b)
elif(ch=="*"):
	print(a*b)
elif(ch=="/"):
	print(a/b)
elif(ch=="%"):
	print(a%b)
else:
	print("INVAILD OPERATOR")
