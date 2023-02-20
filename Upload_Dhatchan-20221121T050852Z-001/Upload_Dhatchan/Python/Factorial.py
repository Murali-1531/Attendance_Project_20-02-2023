def fact(N):
	if(N==0):
		return "Un-Defined"
	elif (N==1):
		return 1
	else:
		return N*fact(N-1)
n=int(input("Enter the number for factoril:"))
print(fact(n))
