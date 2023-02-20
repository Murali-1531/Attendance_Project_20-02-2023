from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
class Auth:
	def login(request):
		return render(request,"index.html")
	def login_data(request):
		name=request.POST["usr"]
		psd=request.POST["psd"]
		check=authenticate(username=name,password=psd)
		print(check)
		if check is not None :
			print("vaild User")
		else:
			print("Invaild User")
		return HttpResponse()
# Create your views here.
