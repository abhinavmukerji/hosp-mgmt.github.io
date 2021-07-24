from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Doctor,Patient,Appointment
import requests
import json
import collections

def About(request):
	return render(request,'about.html')
def Home(request):
	return render(request,'home.html')
def Contact(request):
	return render(request,'contact.html')

def Index(request):
	if not request.user.is_staff:
		return redirect('login.html')
	return render(request,'index.html')
def Login(request):
	error=""
	if request.method=="POST":
		u=request.POST['uname']
		p=request.POST['pwd']
		user=authenticate(username=u,password=p)

		#recaptcha
		clientKey=request.POST['g-recaptcha-response']
		secretKey='6LenSZEaAAAAAMMtUlEBJFrthyvl5hmhGDmfzwgt'	
		capthchaData={'secret':secretKey,'response':clientKey}
		r=requests.post('https://www.google.com/recaptcha/api/siteverify',data=capthchaData)
		response=json.loads(r.text)
		result=response['success']
		print(result)	
		try:
			if user.is_staff and result==True:
				login(request,user)
				error="no"
			else:
				error="yes"
		except:
			error="yes"
	d={'error':error}
	return render(request,'login.html',d)

def Logout_admin(request):
	if not request.user.is_staff:
		return redirect('login')
	logout(request)
	return redirect('admin_login')

def View_doctor(request):
	if not request.user.is_staff:
		return redirect('login')
	doc=Doctor.objects.all()
	d={'doc':doc}
	return render(request,'view_doctor.html',d)

def Delete_Doctor(request,pid):
	if not request.user.is_staff:
		return redirect('login')
	doctor=Doctor.objects.get(id=pid)
	doctor.delete()
	return redirect('view_doctor')

def Add_Doctor(request):
	error=""
	if not request.user.is_staff:
		return redirect('login')
	if request.method=="POST":
		n=request.POST['uname']
		m=request.POST['mobile']
		sp=request.POST['special']
		try:
			if(len(m)!=10):
				error='yes'
			Doctor.objects.create(Name=n,mobile=m,special=sp)
			error='no'			
		except:
			error='yes'
	d={'error':error}
	return render(request,'add_doctor.html',d)

def View_Patient(request):
	if not request.user.is_staff:
		return redirect('login')
	doc=Patient.objects.all()
	d={'doc':doc}
	return render(request,'view_patient.html',d)
def Delete_Patient(request,pid):
	if not request.user.is_staff:
		return redirect('login')
	patient=Patient.objects.get(id=pid)
	patient.delete()
	return redirect('view_patient')

def Add_Patient(request):
	error=""
	if not request.user.is_staff:
		return redirect('login')
	if request.method=="POST":
		n=request.POST['uname']
		g=request.POST['gender']
		m=request.POST['mobile']
		a=request.POST['address']
		try:
			Patient.objects.create(name=n,gender=g,mobile=m,address=a)
			error='no'
			if(len(m)!=10):
				error='yes'
		except:
			error='yes'
	d={'error':error}
	return render(request,'add_patient.html',d)

def Add_Appointment(request):
	error=""
	if not request.user.is_staff:
		return redirect('login')
	doctor1=Doctor.objects.all()
	patient1=Patient.objects.all()
	if request.method=="POST":
		n=request.POST['doctor']
		p=request.POST['patient']
		da=request.POST['date']
		t=request.POST['time']
		doctor=Doctor.objects.filter(Name=n).first()
		patient=Patient.objects.filter(name=p).first()
		try:
			Appointment.objects.create(Doctor=doctor,Patient=patient,date=da,time=t)
			error='no'
		except:
			error='yes'
	d={'doctor':doctor1,'patient':patient1,'error':error}
	return render(request,'add_appointment.html',d)

def View_Appointment(request):
	if not request.user.is_staff:
		return redirect('login')
	doc=Appointment.objects.all()
	d={'doc':doc}
	return render(request,'view_appointment.html',d)

def Delete_Appointment(request,pid):
	if not request.user.is_staff:
		return redirect('login')
	app=Appointment.objects.get(id=pid)
	app.delete()
	return redirect('view_appointment')

#by Abhinav Mukerji(EN18CS301006)