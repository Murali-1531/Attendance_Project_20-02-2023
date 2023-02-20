class emp():
	def __init__(m,name,des):
		m.name=name
		m.des=des
	def Sal_Ch(m):
		if(m.des=="HR"):
			return "Name: "+m.name+" Designation: "+m.des+" Salary: 100000"
		elif(m.des=="Developer"):
			return "Name: "+m.name+" Designation: "+m.des+" Salary: 50000"
		else:
			return "Designation Not Matched"
class emp_inc(emp):
	def Sal_Inc(m):
		if(m.des=="HR"):
			return "Name: "+m.name+" Designation: "+m.des+" Salary: 200000"
		elif(m.des=="Developer"):
			return "Name: "+m.name+" Designation: "+m.des+" Salary: 100000"
		else:
			return "Designation Not Matched"	
name=input("Enter the name:")
des=input("Enter the Designation:")
e=emp(name,des)
print(e.Sal_Ch())
e=emp_inc(name,des)
print(e.Sal_Inc())
