from configparser import ConfigParser
config_obj=ConfigParser()
config_obj["Userinfo"]={"userID":"Murali","loginid":"Murali1531","Password":"1531"}
config_obj["Serverconfig"]={"host":"Murali.com","port":"8080","ipaddr":"8.8.8.8"}
f=open('config.ini', 'w') 
config_obj.write(f)
config_obj.read("config.ini")
usr=config_obj["Userinfo"]
print("User old Password ",usr["Password"])
usr["Password"]="MURALI"
print("User new Password ",usr["Password"])
