from django.shortcuts import render,HttpResponseRedirect,redirect
from django.http import HttpResponse
from django.template import loader
from .models import employee
from django.views.decorators.csrf import csrf_exempt,csrf_protect
class name:
	def murali(request):
		return HttpResponse("Murali Hello")
	def mk(request):
		return HttpResponse("Mk Hello")
	def prem(request):
		return HttpResponse("Prem Hello")
	def Muralihtml(request):
		return render(request,"firsthtml.html")	
class Table:
	def display(request):
		emp=employee.objects.all().values()
		#template=loader.get_template("Table_print.html")
		context={"My_emp":emp,}
		#return HttpResponse(template.render(context)) 
		return render(request,"Table_print.html",context)
	def Data_Enter(request):
		empid=request.GET.get("epid")
		empname=request.GET.get("epname")
		empphone=request.GET.get("ephone")
		emp=employee(eid=empid,ename=empname,ephone=empphone)
		emp.save()
		return HttpResponse("Row Added")
	def edit_data(request,id):
		emp = employee.objects.get(eid = id)
		emp.ename = request.GET.get('epname')
		emp.ephone=request.GET.get('ephone')
		emp.save()
		return HttpResponse("Row Edited")
	def delete_data(request, id):
    		Emp= employee.objects.get(eid=id)
    		Emp.delete()
    		return HttpResponse("Row Deleted ")
    		#return self.display(request)
class css:
	def div_class(request):
		return render(request,"div_class.html")
class auth:
	def login(request):
	 	return render(request,"User_login.html")	


# Create your views here.
