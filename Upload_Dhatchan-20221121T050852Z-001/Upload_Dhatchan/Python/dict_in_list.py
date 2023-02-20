l=[]
nl=int(input("Enter the length of list:"))
nd=int(input("Enter the length of dict:"))
for i in range(nl):
	d={}
	print("Dictonary:",i+1)
	for j in range(nd):
		k=input("Enter The Key:")
		v=input("Enter The Value:")
		d[k]=v
	l.append(d)
print(d)
print(l)
