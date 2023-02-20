from configparser import ConfigParser
con_obj=ConfigParser()
con_obj.read("config.ini")
print("						Login page					")
Userid=input("Enter the UserID:")
pswd=input("Enter the User Password:")
data=con_obj["Userinfo"]
if(data["userid"]==Userid and data["password"]==pswd):
	print("Login successful")
else:
	print("UserID or Password is incorrect")
