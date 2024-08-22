from django.shortcuts import render,redirect,get_object_or_404
from.models import *
from django.contrib.auth import logout

from datetime import datetime, timedelta


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

def viewdoctors(request,uname):
    doctor=doctorreg.objects.all()
    return render(request,'viewdoctors.html',{'uname':uname,'doctor':doctor})

def booking(request,id,uname):
    doctor = get_object_or_404(doctorreg, id=id)
    return render(request, 'booking.html', {'uname': uname, 'doctor': doctor})




def appointment_confirmation(request, id, uname):
    doctor = get_object_or_404(doctorreg, id=id)

    if request.method == 'POST':
        specialty = request.POST['speciality']
        date = request.POST['date']
        start_time_str = request.POST['start_time']

        try:
            start_time = datetime.strptime(start_time_str, '%H:%M').time()
        except ValueError:
            return render(request, 'booking.html', {'uname': uname, 'doctor': doctor, 'error': 'Invalid time format'})

        start_datetime = datetime.combine(datetime.strptime(date, '%Y-%m-%d'), start_time)
        end_datetime = start_datetime + timedelta(minutes=45)

        patient = get_object_or_404(userreg, username=uname)

        # Retrieve all appointments on the same date for this doctor
        existing_appointments = Appointment.objects.filter(
            doctor=doctor,
            date=date
        )

        # Check for overlap
        for appointment in existing_appointments:
            appointment_start = datetime.combine(datetime.strptime(date, '%Y-%m-%d'), appointment.start_time)
            appointment_end = appointment_start + timedelta(minutes=45)

            if (appointment_start < end_datetime and start_datetime < appointment_end):
                return render(request, 'booking.html',
                              {'uname': uname, 'doctor': doctor, 'error': 'Time slot already taken'})

        # If no overlap, create the new appointment
        Appointment.objects.create(
            patient=patient,
            specialty=specialty,
            date=date,
            start_time=start_time,
            doctor=doctor
        )

        return render(request, 'view_appointment.html', {
            'doctor_name': doctor.first_name + ' ' + doctor.last_name,
            'appointment_date': date,
            'start_time': start_time_str,
            'end_time': end_datetime.strftime('%H:%M'),
        })

    return render(request, 'booking.html', {'uname': uname, 'doctor': doctor})


def view_doctor_appointments(request, uname):
    doctor = get_object_or_404(doctorreg, username=uname)

    # Query appointments for this doctor
    appointments = Appointment.objects.filter(doctor=doctor).order_by('date', 'start_time')

    # Calculate end times for each appointment
    appointments_with_end_times = []
    for appointment in appointments:
        start_datetime = datetime.combine(appointment.date, appointment.start_time)
        end_datetime = start_datetime + timedelta(minutes=45)
        appointment_end_time = end_datetime.time()
        appointments_with_end_times.append({
            'appointment': appointment,
            'end_time': appointment_end_time
        })

    return render(request, 'view_appointment_events.html', {
        'doctor': doctor,
        'appointments_with_end_times': appointments_with_end_times
    })


# def book_appointment(request, doctor_id):
#     doctor = get_object_or_404(doctorreg, id=doctor_id)
#     if request.method == 'POST':
#         patient_name = request.POST['patient_name']
#         date = request.POST['date']
#         start_time = request.POST['start_time']
#         end_time = (datetime.datetime.strptime(start_time, '%H:%M') + timedelta(minutes=45)).time()
#
#         appointment = Appointment.objects.create(
#             doctor=doctor,
#             patient_name=patient_name,
#             date=date,
#             start_time=start_time,
#             end_time=end_time
#         )
#
#         # Create Google Calendar event
#         start_datetime = datetime.datetime.combine(datetime.date.fromisoformat(date), start_time)
#         end_datetime = datetime.datetime.combine(datetime.date.fromisoformat(date), end_time)
#         create_calendar_event(
#             doctor.email,
#             f"Appointment with {patient_name}",
#             f"Appointment for {patient_name}",
#             start_datetime,
#             end_datetime
#         )
#
#         return render(request, 'appointment_confirmation.html', {'appointment': appointment})
#
#     return render(request, 'book_appointment.html', {'doctor': doctor})
#
# def view_doctor_appointments(request, username):
#     doctor = get_object_or_404(doctorreg, username=username)
#     events = get_doctor_calendar_events(doctor.email)
#     return render(request, 'view_doctor_appointments.html', {'events': events})
#
