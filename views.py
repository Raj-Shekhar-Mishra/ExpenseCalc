from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User,Expense,Income
def loginPage(req):
	return render(req,"login.html")

def register(req):
	return render(req,"register.html")

def expensePage(req):
	return render(req,"addexpense.html")

def incomePage(req):
	return render(req,"addincome.html")

def saveData(req):
	obj=User()
	obj.name=req.GET.get('name')
	obj.password=req.GET.get('password')
	obj.mobile=req.GET.get('mobile')
	obj.address=req.GET.get('address')
	obj.save()
	return redirect('/loginPage')

def saveExpense(req):
	obj=Expense()
	id=req.session['id']
	obj.date=req.GET.get('date')
	obj.remark=req.GET.get('remark')
	obj.category=req.GET.get('category')
	obj.amount=req.GET.get('amount')
	obj.user_id=id
	obj.save()
	return render(req,"addexpense.html")

def saveIncome(req):
	obj=Income()
	id=req.session['id']
	obj.date=req.GET.get('date')
	obj.remark=req.GET.get('remark')
	obj.category=req.GET.get('category')
	obj.amount=req.GET.get('amount')
	obj.user_id=id
	obj.save()
	return render(req,"addincome.html")

def dashboard(req):
	if 'id' in req.session:
		id=req.session['id']
		expense=Expense.objects.filter(user_id=id)
		income=Income.objects.filter(user_id=id)
		NetBalance=0
		TotalExpense=0
		TotalIncome=0


		food=0
		cloth=0
		fuel=0
		traveling=0

		salary=0
		rent=0
		stock=0
		shop=0
		for exp in expense:
			TotalExpense+=exp.amount
			if 'food' in exp.category:
				food+=exp.amount
			if 'cloth' in exp.category:
				cloth+=exp.amount
			if 'fuel' in exp.category:
				fuel+=exp.amount
			if 'traveling' in exp.category:
				traveling+=exp.amount
				
		for inc in income:
			TotalIncome+=inc.amount
			if 'salary' in inc.category:
				salary+=inc.amount
			if 'rent' in inc.category:
				rent+=inc.amount
			if 'stock' in inc.category:
				stock+=inc.amount
			if 'shop' in inc.category:
				shop+=inc.amount
			


		NetBalance=TotalIncome-TotalExpense
		if(NetBalance>0):
			return render(req,"dashboard.html",{'NetBalance':NetBalance,'TotalExpense':TotalExpense,'TotalIncome':TotalIncome,'Food':food,'Cloth':cloth,'Fuel':fuel,'Traveling':traveling,'Salary':salary,'Rent':rent,'Stock':stock,'Shop':shop})
		else:
			return render(req,"dashboard.html",{'NetBalance':'Low Balance','TotalExpense':TotalExpense,'TotalIncome':TotalIncome})

	return render(req,"dashboard.html")

def checkLogin(req):
	name=req.POST.get('name')
	passs=req.POST.get('pass')
	record=User.objects.filter(name=name,password=passs)
	if(record):
		data=record.values()
		req.session['id']=data[0]['id']
		req.session['name']=data[0]['name']
		return redirect('/dashboard')
	else:
		return render(req,"login.html")

def logout(req):
	del req.session['id']
	del req.session['name']
	return render(req,"login.html")

def allExpense(req):
	id=req.session['id']
	record=Expense.objects.filter(user_id=id)
	return render(req,"allexpense.html",{'record':record})

def allIncome(req):
	id=req.session['id']
	record=Income.objects.filter(user_id=id)
	return render(req,"allincome.html",{'record':record})

