from django.db import models
class User(models.Model):
	name=models.CharField(max_length=50)
	password=models.CharField(max_length=10)
	mobile=models.CharField(max_length=10)
	address=models.CharField(max_length=50)
	class Meta:
		db_table='user'

class Expense(models.Model):
	date=models.DateField()
	remark=models.CharField(max_length=50)
	category=models.CharField(max_length=50)
	amount=models.FloatField()
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	class Meta:
		db_table='expense'

class Income(models.Model):
	date=models.DateField()
	remark=models.CharField(max_length=50)
	category=models.CharField(max_length=50)
	amount=models.FloatField()
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	class Meta:
		db_table='income'
