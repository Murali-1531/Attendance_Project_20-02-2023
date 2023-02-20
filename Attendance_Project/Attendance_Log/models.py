from django.db import models
from django.conf import settings
class Student_Details_UG(models.Model):
	User_Name=models.CharField(max_length=100,primary_key=True)
	Regno=models.CharField(max_length=100,unique=True)
	Name=models.CharField(max_length=100)
	DOB=models.DateField()
	Gender=models.CharField(max_length=50)
	Degree=models.CharField(max_length=100)
	Year=models.CharField(max_length=100,default="N/A")
	Department=models.CharField(max_length=100)
	Phone_Number=models.BigIntegerField()
	Mail_ID=models.EmailField(max_length = 254,unique=True)
	class Meta:
		db_table="Student_Details_UG"
class Student_Details_PG(models.Model):
	User_Name=models.CharField(max_length=100,primary_key=True)
	Regno=models.CharField(max_length=100,unique=True)
	Name=models.CharField(max_length=100)
	DOB=models.DateField()
	Gender=models.CharField(max_length=50)
	Degree=models.CharField(max_length=100)
	Year=models.CharField(max_length=100,default="N/A")
	Department=models.CharField(max_length=100)
	Phone_Number=models.BigIntegerField()
	Mail_ID=models.EmailField(max_length = 254,unique=True)
	class Meta:
		db_table="Student_Details_PG"
class Staff_Details(models.Model):		
	User_Name=models.CharField(max_length=100,primary_key=True)
	Staff_ID=models.CharField(max_length=50,unique=True)
	Name =models.CharField(max_length=100)
	Department =models.CharField(max_length=100)
	Phone_Number=models.BigIntegerField()
	Mail_ID=models.EmailField(max_length = 254,unique=True)
	Photo=models.ImageField(upload_to ='Staff_Images/')	
	class Meta:
		db_table="Staff_Details"
class OTP(models.Model):		
	User_Name=models.CharField(max_length=100,primary_key=True)
	Otp=models.IntegerField(unique=True)
	class Meta:
		db_table="OTP"	 	 
class UG_Students_Attendance(models.Model):
	Markers_ID=models.CharField(max_length=100,null = False)
	Student_Regno=models.ForeignKey("Student_Details_UG",to_field="Regno",on_delete=models.CASCADE)
	Student_Name=models.CharField(max_length=100,null = False)
	Date=models.DateField()
	HR_1=models.CharField(max_length=10)
	HR_2=models.CharField(max_length=10)
	HR_3=models.CharField(max_length=10)
	HR_4=models.CharField(max_length=10)
	HR_5=models.CharField(max_length=10)
	class Meta:
		db_table="UG_Students_Attendance"
class PG_Students_Attendance(models.Model):
	Markers_ID=models.CharField(max_length=100,null = False)
	Student_Regno=models.ForeignKey("Student_Details_PG",to_field="Regno",on_delete=models.CASCADE)
	Student_Name=models.CharField(max_length=100,null = False)
	Date=models.DateField()
	HR_1=models.CharField(max_length=10)
	HR_2=models.CharField(max_length=10)
	HR_3=models.CharField(max_length=10)
	HR_4=models.CharField(max_length=10)
	HR_5=models.CharField(max_length=10)
	class Meta:
		db_table="PG_Students_Attendance"		

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
# Create your models here. 
