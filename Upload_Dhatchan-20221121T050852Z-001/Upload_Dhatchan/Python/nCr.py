def fact(N):
	if(N==0):
		return "Un-Defined"
	elif(N==1):
		return 1
	else:
		return N*fact(N-1)
n,r=input("Enter the n and r value respectively for nCr:").split()
print("The N value:",n)
print("The R value:",r)
n=int(n)
r=int(r)
nf=fact(n)
rf=fact(r)
nrf=fact(n-r)
print(n,"C",r,"=",(fact(n)/(fact(r)*fact(n-r))))
