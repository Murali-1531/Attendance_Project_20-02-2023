d={}
n=int(input("Enter the length of Dict:"))
for i in range(n):
	k=input("Enter the key:")
	v=input("Enter the value:")
	d[k]=v
print(d)
c=input("Enter the key of value you want to update:")
name=input("Enter the value to update:")
d[c]=name
print(d)
D=input("Enter the key to delete")
print(d.pop(D))
print(d)

