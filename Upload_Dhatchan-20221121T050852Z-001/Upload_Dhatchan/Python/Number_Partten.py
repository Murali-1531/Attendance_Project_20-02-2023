n=int(input("Enter the n value:"))
c=0
for i in range(n):
	for j in range (i+1):
		c+=1		
		print(c,end=" ")
	print()
