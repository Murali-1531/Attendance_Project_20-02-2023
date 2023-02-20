frd=["Murali","MK","Prem","Aravinth"]
print("1-->Display  2--> Add friend 3--> Modify 4--> Delete 5-->Check")
ch=int(input("Enter the your choice:"))
if(ch==1):
	for i in frd:
		print (i)
elif(ch==2):
	name=input("Enter the name you want to add:")
	frd.append(name)
	for i in frd:
		print (i)
elif(ch==3):
	for i in range(len(frd)):
		print (frd[i],"-->",i)
	n=int(input("Enter the number equal to name as shown in above :"))
	name=input("Enter the  new name :")
	frd[n]=name
	for i in frd:
		print (i)
elif(ch==4):	
	for i in range(len(frd)):
		print (frd[i],"-->",i)
	n=int(input("Enter the number equal to name as shown in above to Delete:"))
	frd.pop(n)	
	for i in frd:
		print (i)
elif(ch==5):
	name=input("Enter the name you want to check:")
	if name in frd:
		print("Yes it there")
	else:
		print("It is not there")
else:
	print("Choice out of bound ")
