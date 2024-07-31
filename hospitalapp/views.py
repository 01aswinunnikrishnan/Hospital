from django.shortcuts import render,redirect
from.models import *
from django.contrib.auth import logout

def signup(request):
    return render(request,'signup.html')

def signingup(request):
    if request.method=='POST':
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        profilepic=request.FILES['photo']
        uname=request.POST['uname']
        gmail=request.POST['email']
        pasw=request.POST['pas']
        cpasw=request.POST['cpas']
        address=request.POST['address']
        if pasw != cpasw:
            return render(request, 'signup.html', {'error': 'Passwords do not match'})
        data=userreg.objects.create(first_name=firstname,last_name=lastname,profilepic=profilepic,username=uname,email=gmail,Password=pasw,address=address)
        data.user = request.user 
        data.save()
        return redirect(logpg)
    return render(request,'signup.html')

def doc_signingup(request):
    if request.method=='POST':
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        profilepic=request.FILES['photo']
        uname=request.POST['uname']
        gmail=request.POST['email']
        pasw=request.POST['pas']
        cpasw=request.POST['cpas']
        address=request.POST['address']
        if pasw != cpasw:
            return render(request, 'doctorsignup.html', {'error': 'Passwords do not match'})
        data=doctorreg.objects.create(first_name=firstname,last_name=lastname,profilepic=profilepic,username=uname,email=gmail,Password=pasw,address=address)
        data.user = request.user 
        data.save()
        return redirect(logpg)
    return render(request,'doctorsignup.html')


def logpg(request):
    return render(request,'login.html')

def login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        password = request.POST['pas']
        data=userreg.objects.filter(username=uname)
        doc_data=doctorreg.objects.filter(username=uname)
        
        if data:
            data1=userreg.objects.get(username=uname)
            if data1.Password==password:
                request.session['id']=uname
                return redirect(patient_profile,u=uname)
            else:
                return render(request, 'login.html', {'error': 'User Has No Account'})
        elif doc_data:
            doc_data1=doctorreg.objects.get(username=uname)
            if doc_data1.Password==password:
                request.session['id']=uname
                return redirect(doctor_profile,u=uname)
            else:
                return render(request, 'login.html', {'error': 'User Has No Account'})
        else:
            return render(request, 'login.html', {'error': 'User Has No Account'})
    


def patient_profile(request,u):
    d1=userreg.objects.filter(username=u)
    return render(request,'patienthm.html',{'data1':d1,'username':u})

def doctor_profile(request,u):
    d1=doctorreg.objects.filter(username=u)
    return render(request,'doctorhm.html',{'data1':d1,'username':u})

def user_logout(request):
    logout(request)
    return redirect(logpg)


# Create your views here.
