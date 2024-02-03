from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from .models import Profile,Image,Patient,Appointment
from django.contrib.auth.decorators import login_required
from .forms import ImageForm
# Create your views here.

def index(req):
    return render(req, 'home.html')

def signup(req):
    if req.method=='POST':
        username=req.POST.get('username')
        password=req.POST.get('password')
        email=req.POST.get('email')
        
        if User.objects.filter(email=email).exists():
            messages.info(req,'Email taken')
            return redirect('signup')
        elif User.objects.filter(username=username).exists():
            messages.info(req,'username taken')
            return redirect('signup')
        else:
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save()

            #create profile object
            user_model=User.objects.get(username=username)
            new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
            new_profile.save()
            return redirect('signup')
    else:
        return render(req,'signup.html')

def signin(req):
    if req.method=='POST':
        username=req.POST.get('username')
        password=req.POST.get('password')

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(req, user)
            return redirect('/')
        else:
            messages.info(req,'Credentials Invalid')
            return redirect('signin')
    else:
        return render(req,'signin.html')

def logout(req):
    auth.logout(req)
    return redirect('signin')
      
def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'upload.html',{'form': form,'img_obj':img_obj})
    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form})

def image_list(req):
    images=Image.objects.all()
    return render(req,'image_list.html',{'images':images})

def doctors(req):
    return render(req,'doctors.html')


def appointment(request):
    if request.method == 'POST':
        patient_name = request.POST['name']
        appointment_date = request.POST['date']

        patient = Patient.objects.create(name=patient_name)
        appointment = Appointment(patient=patient, appointment_date=appointment_date)
        appointment.save()
        messages.success(request, 'Appointment created successfully.')
        return redirect('appointment')

    return render(request, 'appointment.html')

def delete(req):
     if req.method == 'POST':
        name = req.POST['username']
        user = User.objects.get(username=name)
        user.delete()
     return render(req,'delete.html')