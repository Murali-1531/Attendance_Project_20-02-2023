from django.db import models
class employee(models.Model):
	eid=models.CharField(max_length=20)
	ename=models.CharField(max_length=100)
	ephone=models.IntegerField()
	class Meta:
		db_table="Employee"
# Create your models here.
