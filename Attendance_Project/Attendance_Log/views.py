from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.template import loader
from django.contrib.auth import authenticate,login
from .models import Staff_Details,OTP,Student_Details_UG,Student_Details_PG,UG_Students_Attendance,PG_Students_Attendance
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.conf import settings
import random,datetime
class login_form:
	def login(request):
		username=request.POST.get("usr")
		password=request.POST.get("psd")	
		user = authenticate(username=username, password=password)	
		if user is not None:		
			login(request,user)
			if(user.groups.filter(name='Admin').exists()):		
				return render(request,"Admin_Home_Page.html")
			elif(user.groups.filter(name='Staff_Group').exists()):
				Staff=Staff_Details.objects.all().filter(User_Name=user)
				context={'Staff_det':Staff}
				return render(request,"Staff_Home_Page.html",context)
			else:
				return render(request,"text.html")
		else:
			context={'title': 'Invalid Username or Password'}
			return render(request, 'index.html',context)
	def forgot_password(request):
    		data=request.GET.get("usr_name")  	    		
    		try:
    			user=User.objects.get(username=data)
    			mail_to=[]
    			mail_to.append(user.email) 		    		
    			res = user.email[1:user.email.index('@')]
    			if(len(res)<=4):
    				res=res[len(res)-3:]
    			else:
    				res=res[len(res)-4:]	    	    			
    			randomNumber = random.randint(1000,9999)
    			subject = 'One Time Password For Your Account'
    			message = 'Your OTP Is=>'+str(randomNumber)
    			email_from = settings.EMAIL_HOST_USER   		
    			send_mail( subject, message, email_from, mail_to)    				
    			Otp=OTP(User_Name=data,Otp=randomNumber)
    			Otp.save()
    			context={'email':res,'user_name':data}
    			return render(request,"OTP_Ver.html",context)  	
    		except Exception as e:  
    			context={'title': ' Username Not Found'}
    			return render(request, 'index.html',context)			
	def Ver_Otp(request):
		otp=request.POST.get("otp_no-1")
		otp+=request.POST.get("otp_no-2")
		otp+=request.POST.get("otp_no-3")
		otp+=request.POST.get("otp_no-4")
		user_name=request.POST.get("user_name")
		Otp_tb=OTP.objects.get(User_Name=user_name)		
		if(otp==str(Otp_tb.Otp)):			
			Otp_tb.delete()
			context={'user_name':user_name}
			return render(request,"Password_Change.html",context) 
		else:	
			context={"result":"Invaild OTP",'user_name':user_name}
			return render(request,"OTP_Ver.html",context)			  	 
	def change_password(request):	
    		new_password=request.POST.get("password")
    		user_name=request.POST.get("user_name")
    		user=User.objects.get(username=user_name)
    		user.set_password(new_password)
    		user.save()
    		return render(request,'index.html')	  			
class Staff_All:
	def Display_Staff(request):
		Staff=Staff_Details.objects.all().values()
		#template=loader.get_template("Table_print.html")
		context={"Staff_det":Staff}
		#return HttpResponse(template.render(context)) 
		return render(request,"Display_Staff_Info.html",context)
	def Add_Staff(request): 
		all_users=User.objects.all().values('username')
		all_users=list(all_users)
		user=[]
		for i in range (len(all_users)):
			user.append(all_users[i]["username"])
		context={'title':user}		
		if request.method == 'POST' and request.FILES['upload']:
			upload = request.FILES['upload']
			fss = FileSystemStorage()
			file = fss.save('images/Staff_Images/'+upload.name, upload)
			file_url = fss.url(file)
			User_Name=request.POST.get("User_Name")
			User_password=request.POST.get("User_Password")
			staff_id=request.POST.get("Staff ID")
			staff_name=request.POST.get("Staff Name")
			staff_dep=request.POST.get("Staff Department")
			staff_Mail=request.POST.get("Staff Mail_ID")
			staff_Phone=request.POST.get("Staff Phone_No")			
			staff=Staff_Details(User_Name=User_Name,
			Staff_ID=staff_id,Name=staff_name,
			Department=staff_dep,Mail_ID=staff_Mail,
			Photo='images/Staff_Images/'+upload.name,Phone_Number=staff_Phone)
			user=User.objects.create_user(username=User_Name,
			first_name=staff_name,email=staff_Mail,
			password=User_password)
			Grouped = Group.objects.get(name="Staff_Group") 
			user.groups.add(Grouped)
			staff.save()
			user.save()	
			return render(request, 'Staff_Info.html',context)
		return render(request, 'Staff_Info.html',context)
	def Update_Staff(request):
		ID=request.POST.get("tsid")
		user_name=request.POST.get("usr_name")
		user=User.objects.get(username=user_name)
		user.first_name=request.POST.get("tsname")
		user.email=request.POST.get("tsmail")
		user.save()		
		staff = Staff_Details.objects.get(Staff_ID =ID)
		staff.Name=request.POST.get("tsname")
		staff.Department=request.POST.get("tsdep")
		staff.Mail_ID=request.POST.get("tsmail")
		staff.Phone_Number=request.POST.get("tsphone")	
		staff.save()
		return HttpResponse("Row Edited")
	def Remove_Staff(request):
		usr_name=request.POST.get("usr_name")
		staff = Staff_Details.objects.get(User_Name=usr_name)
		staff.delete()
		ID=User.objects.get(username=usr_name).pk
		Grouped = Group.objects.get(name="Staff_Group")
		Grouped.user_set.remove(ID)
		user = User.objects.filter(username=usr_name)
		user.delete()
		return HttpResponse("Row Deleted")
	def Back_to_Admin(request):
		return render(request,"Admin_Home_Page.html")	
class Student_All:
	def Student(request):		
		return render(request,"Student.html")
	def Display_Student(request):
		grad=request.POST.get("Grad")
		year=request.POST.get("Year")
		dep=request.POST.get("Dep")
		Grad=request.GET.get("degree")
		Year=request.GET.get("year")
		Dep=request.GET.get("dep")
		if grad:
			if(year=="First Year(I)"):
				year="I"
			elif(year=="Second Year(II)"):
				year="II"
			else:
				year="III"
			if(grad=="Under Graduate(UG)"):
				grad="UG"
				Student=Student_Details_UG.objects.filter(Year=year,Department=dep).values()
			else:
				grad="PG"
				Student=Student_Details_PG.objects.filter(Year=year,Department=dep).values()				
			context={"Student_det":Student,"Grad":grad,"Year":year,"Dep":dep}
		else:
			if(Grad=="UG"):
				Student=Student_Details_UG.objects.filter(Year=Year,Department=Dep).values()
			else:
				Student=Student_Details_PG.objects.filter(Year=Year,Department=Dep).values()
			context={"Student_det":Student,"Grad":Grad,"Year":Year,"Dep":Dep}
		return render(request,"Display_Student_Info.html",context)
	def Add_Student(request): 
		all_users=User.objects.all().values('username')
		all_users=list(all_users)
		user=[]		
		for i in range (len(all_users)):
			user.append(all_users[i]["username"])
		context={'title':user}			
		if request.method == 'POST':
			grad=request.POST.get("degree")
			
			year=request.POST.get("year")
			dep=request.POST.get("dep")
			User_Name=request.POST.get("User_Name")
			User_password=request.POST.get("User_Password")
			reg_no=request.POST.get("Student Reg")
			name=request.POST.get("Student Name")
			DOB=request.POST.get("Student DOB")
			gender=request.POST.get("Gender")
			degree=request.POST.get("Degree")
			year=request.POST.get("year")
			dep=request.POST.get("Student Department")
			Mail=request.POST.get("Student Mail_ID")
			Phone=request.POST.get("Student Phone_No")
			context={'title':user,'Grad':grad,'Year':year,'Dep':dep}			
			if(degree=="UG"):
				student=Student_Details_UG(
				User_Name=User_Name,
				Regno=reg_no,Name=name,DOB=DOB,
				Gender=gender,Degree=degree,
				Year=year,Department=dep,
				Phone_Number=Phone,Mail_ID=Mail)
			else:
				student=Student_Details_PG(
				User_Name=User_Name,
				Regno=reg_no,Name=name,DOB=DOB,
				Gender=gender,Degree=degree,
				Year=year,Department=dep,
				Phone_Number=Phone,Mail_ID=Mail)
			user=User.objects.create_user(username=User_Name,
			first_name=name,email=Mail,
			password=User_password)
			Grouped = Group.objects.get(name="Student_Group") 
			user.groups.add(Grouped)
			student.save()
			user.save()
			return render(request,'Student_Info.html',context)
		return render(request,'Student_Info.html',context)
	def Update_Student(request):
		regno=request.POST.get("streg")
		Grad=request.POST.get("Grad")
		user_name=request.POST.get("usr_name")
		user=User.objects.get(username=user_name)
		user.first_name=request.POST.get("stname")
		user.email=request.POST.get("stmail")
		user.save()
		if(Grad=="UG"):
			student=Student_Details_UG.objects.get(Regno=regno)		
			student.Name=request.POST.get("stname")
			student.DOB=request.POST.get("stDOB")
			student.Gender=request.POST.get("stgen")
			student.Mail_ID=request.POST.get("stmail")
			student.Phone_Number=request.POST.get("stphone")	
			student.save()			
		if(Grad=="PG"):
			student=Student_Details_PG.objects.get(Regno=regno)		
			student.Name=request.POST.get("stname")
			student.DOB=request.POST.get("stDOB")
			student.Gender=request.POST.get("stgen")
			student.Mail_ID=request.POST.get("stmail")
			student.Phone_Number=request.POST.get("stphone")	
			student.save()
		return HttpResponse("Row Edited")
	def Remove_Student(request):
		usr_name=request.POST.get("usr_name")
		Degree=request.POST.get("degree")
		if(Degree=="UG"):
			student = Student_Details_UG.objects.get(User_Name=usr_name)
		else:
			student = Student_Details_PG.objects.get(User_Name=usr_name)
		student.delete()
		ID=User.objects.get(username=usr_name).pk
		Grouped = Group.objects.get(name="Student_Group")
		Grouped.user_set.remove(ID)
		user = User.objects.filter(username=usr_name)
		user.delete()
		return HttpResponse("Row Deleted")
	def Admin_Edit_Attendance(request):
		grad=request.GET.get("degree")
		year=request.GET.get("year")
		dep=request.GET.get("dep")
		context={"Grad":grad,"Year":year,"Dep":dep}
		if request.method == 'POST':
			grad=request.POST.get("grad")
			year=request.POST.get("year")
			dep=request.POST.get("dep")
			date=request.POST.get("date")
			regno=request.POST.get("Regno")
			print(grad	,year,dep,date,regno)
			if(grad=="UG"):
				Student=UG_Students_Attendance.objects.filter(Date=date,Student_Regno_id=regno).values()
				context={"Student_det":list(Student)}
			else:
				Student=PG_Students_Attendance.objects.filter(Date=date,Student_Regno_id=regno).values()
				context={"Student_det":list(Student)}
			return JsonResponse(context)
		return render(request,"Student_Edit_Attendance.html",context)
	def Admin_Edited_Mark_Attendance(request):
		HR_1=request.POST.get("HR_1")
		HR_2=request.POST.get("HR_2")
		HR_3=request.POST.get("HR_3")
		HR_4=request.POST.get("HR_4")
		HR_5=request.POST.get("HR_5")
		grad=request.POST.get("grad")
		year=request.POST.get("year")
		dep=request.POST.get("dep")
		regno=request.POST.get("Regno")
		date=request.POST.get("Date")
		context={"Grad":grad,"Year":year,"Dep":dep}
		print(HR_1,HR_2,HR_3,HR_4,HR_5,grad,year,dep,regno,date)
		if(grad=="UG"):
			if(HR_1=="on" and HR_2=="on" and HR_3=="on" and HR_4=="on" and HR_5=="on"):
				Attendance = UG_Students_Attendance.objects.filter(Date=date,Student_Regno_id=regno)
				Attendance.delete()
			else:
				if(HR_1=="on"):
					Attendance=UG_Students_Attendance.objects.get(Date=date,Student_Regno_id=regno)		
					Attendance.HR_1="-"
					Attendance.save()
				else:
					Attendance=UG_Students_Attendance.objects.get(Date=date,Student_Regno_id=regno)		
					Attendance.HR_1="AB"
					Attendance.save()
				if(HR_2=="on"):
					Attendance=UG_Students_Attendance.objects.get(Date=date,Student_Regno_id=regno)		
					Attendance.HR_2="-"
					Attendance.save()
				else:
					Attendance=UG_Students_Attendance.objects.get(Date=date,Student_Regno_id=regno)		
					Attendance.HR_2="AB"
					Attendance.save()
				if(HR_3=="on"):
					Attendance=UG_Students_Attendance.objects.get(Date=date,Student_Regno_id=regno)		
					Attendance.HR_3="-"
					Attendance.save()
				else:
					Attendance=UG_Students_Attendance.objects.get(Date=date,Student_Regno_id=regno)		
					Attendance.HR_3="AB"
					Attendance.save()
				if(HR_4=="on"):
					Attendance=UG_Students_Attendance.objects.get(Date=date,Student_Regno_id=regno)		
					Attendance.HR_4="-"
					Attendance.save()
				else:
					Attendance=UG_Students_Attendance.objects.get(Date=date,Student_Regno_id=regno)		
					Attendance.HR_4="AB"
					Attendance.save()
				if(HR_5=="on"):
					Attendance=UG_Students_Attendance.objects.get(Date=date,Student_Regno_id=regno)		
					Attendance.HR_5="-"
					Attendance.save()
				else:
					Attendance=UG_Students_Attendance.objects.get(Date=date,Student_Regno_id=regno)		
					Attendance.HR_5="AB"
					Attendance.save()
		if(grad=="PG"):	
			if(HR_1=="on" and HR_2=="on" and HR_3=="on" and HR_4=="on" and HR_5=="on"):
				Attendance =PG_Students_Attendance.objects.filter(Date=date,Student_Regno_id=regno)
				Attendance.delete()
			else:
				if(HR_1=="on"):
					Attendance=PG_Students_Attendance.objects.get(Date=date,Student_Regno_id=regno)		
					Attendance.HR_1="-"
					Attendance.save()
				else:
					Attendance=PG_Students_Attendance.objects.get(Date=date,Student_Regno_id=regno)		
					Attendance.HR_1="AB"
					Attendance.save()
				if(HR_2=="on"):
					Attendance=PG_Students_Attendance.objects.get(Date=date,Student_Regno_id=regno)		
					Attendance.HR_2="-"
					Attendance.save()
				else:
					Attendance=PG_Students_Attendance.objects.get(Date=date,Student_Regno_id=regno)		
					Attendance.HR_2="AB"
					Attendance.save()
				if(HR_3=="on"):
					Attendance=PG_Students_Attendance.objects.get(Date=date,Student_Regno_id=regno)		
					Attendance.HR_3="-"
					Attendance.save()
				else:
					Attendance=PG_Students_Attendance.objects.get(Date=date,Student_Regno_id=regno)		
					Attendance.HR_3="AB"
					Attendance.save()
				if(HR_4=="on"):
					Attendance=PG_Students_Attendance.objects.get(Date=date,Student_Regno_id=regno)		
					Attendance.HR_4="-"
					Attendance.save()
				else:
					Attendance=PG_Students_Attendance.objects.get(Date=date,Student_Regno_id=regno)		
					Attendance.HR_4="AB"
					Attendance.save()
				if(HR_5=="on"):
					Attendance=PG_Students_Attendance.objects.get(Date=date,Student_Regno_id=regno)		
					Attendance.HR_5="-"
					Attendance.save()
				else:
					Attendance=PG_Students_Attendance.objects.get(Date=date,Student_Regno_id=regno)		
					Attendance.HR_5="AB"
					Attendance.save()
		return render(request,"Student_Edit_Attendance.html",context)
			
# Create your viwes here.conte    



    
