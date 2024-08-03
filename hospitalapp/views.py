from django.shortcuts import render,redirect,get_object_or_404
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
        else:
            data=userreg.objects.create(first_name=firstname,last_name=lastname,profilepic=profilepic,username=uname,email=gmail,Password=pasw,address=address)
            data.user = request.user
            data.save()
            return redirect(logpg)
    else:
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
        else:
            data=doctorreg.objects.create(first_name=firstname,last_name=lastname,profilepic=profilepic,username=uname,email=gmail,Password=pasw,address=address)
            data.user = request.user
            data.save()
            return redirect(logpg)
    else:
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
    return render(request,'patienthm.html',{'data1':d1,'uname':u})

def doctor_profile(request,u):
    d1=doctorreg.objects.filter(username=u)
    return render(request,'doctorhm.html',{'data1':d1,'uname':u})

def user_logout(request):
    logout(request)
    return redirect(logpg)

def addblog(request,uname):
    categories = Category.objects.all()
    return render(request,'addblogs.html',{'uname':uname,'categories':categories})

def add_blog(request,uname):
    if request.method=='POST':
        title=request.POST['title']
        image=request.FILES['image']
        category=request.POST['category']
        summary=request.POST['summary']
        content=request.POST['content']
        is_draft='is_draft' in request.POST
        categories=Category.objects.get(id=category)
        doctor = get_object_or_404(doctorreg,username=uname)
        data=Blogs.objects.create(author=doctor,title=title,image=image,category=categories,summary=summary,content=content,is_draft=is_draft)
        data.save()
        return redirect(addblog,uname=uname)

def doctorblog(request,uname):
    author = get_object_or_404(doctorreg,username=uname)
    blog=Blogs.objects.filter(author=author,is_draft=False)
    return render(request,'viewyourblog.html',{'uname':uname,'blog':blog})

def draft_blogs(request,uname):
    author = get_object_or_404(doctorreg,username=uname)
    draft=Blogs.objects.filter(author=author,is_draft=True)
    return render(request,'draftblogs.html',{'uname':uname,'draft':draft})

def view_post(request,uname):
    posts = Blogs.objects.filter(is_draft=False)
    posts_category = {}
    for post in posts:
        if post.category not in posts_category:
            posts_category[post.category] = []
        posts_category[post.category].append(post)
    categories=Category.objects.all()
    return render(request,'viewallblogs.html',{'uname':uname,'post':posts,'posts_category':posts_category,'categories':categories})





# Create your views here.
