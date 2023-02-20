function login_check()
{
	usr=document.getElementById("usr");
	username=usr.value;
	pwd=document.getElementById("pwd");
	password=pwd.value;
	if(username=="Murali" && password=="1531" )
	{
		alert("Welcome Admin");
		return true;
	}
	else
	{
		alert("Invalid User Name or Password");
		return false;
	}
}
