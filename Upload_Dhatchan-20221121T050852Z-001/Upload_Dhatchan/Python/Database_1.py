from mysql.connector import connect as co
mydb=co(host="localhost",database="Sample",user="root",password="root")	
q1="insert into student(name,regno,age,department) values(%s,%s,%s,%s);"
n=int(input("Enter the No of rows you want to enter:"))
l=[]
c=1
for i in range(n):
	print("Row:",c)
	z=[]
	tn=input("Enter the name:")
	z.append(tn)
	tr=input("Enter the regno:")
	z.append(tr)
	ta=int(input("Enter the age:"))
	z.append(ta)
	td=input("Enter the department:")
	z.append(td)
	l.append(z)
	c+=1
q2="select * from student;"
mycursor=mydb.cursor()
mycursor.executemany(q1,l)
mycursor.execute(q2)
for i in mycursor:
	print(i) 
mydb.commit()
