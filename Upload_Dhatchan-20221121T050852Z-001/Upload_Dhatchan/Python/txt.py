#from configparser import ConfigParser
#config_obj=ConfigParser()
#config_obj["Userinfo"]={"userID":"Murali","loginid":"Murali1531","Password":"1531"}
#config_obj["Serverconfig"]={"host":"Murali.com","port":"8080","ipaddr":"8.8.8.8"}
#f=open('config.ini', 'w') 
#config_obj.read("'config.ini")
#usr=config_obj["Userinfo"]
#for i in usr:
#	print(i,"->",usr[i])
#print("				Login page				")
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
print(l)
