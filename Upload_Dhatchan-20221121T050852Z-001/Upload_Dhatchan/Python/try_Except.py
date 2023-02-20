a=int(input("Enter the value of A:"))
b=int(input("Enter the value of B:"))
try:
	print(a/b)
#except ZeroDivisionError:
#	print(" No zero value for B")
#except ValueError:
#	print("Error")	
except:
	print("Exception Occured")
else:
	print("Else block running")
finally:
	print("Final block rnning")
