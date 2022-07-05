from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Report

# Create your views here.

def index(request):
    return render(request,'base.html') 

def handleSignup(request):
    if request.method == 'POST':
        # Get the post parameters
        uncode = request.POST['unicode']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # Check for erroneous inputs
        if pass1 != pass2:
            messages.error(request,'Passwords do not match')
            return redirect('home')

        # create user
        myuser = User.objects.create_user(uncode,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,'Your Crmap account has been successfully create')
        return redirect('home')
    else:
        return HttpResponse('404-Not Found')

def handleLogin(request):
    if request.method == 'POST':
        #Get the post parameters
        loginuncode= request.POST['ucode'] 
        loginpasswd= request.POST['pass']

        user = authenticate(username=loginuncode,password= loginpasswd)

        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged In")
            return render(request,'login.html')
        else:
            messages.error(request,"Invalid Credentials,Please try again")
            return redirect('home')
    else:
        return redirect('home')

def handleLogout(request):
    return HttpsResponse("LOGOUT")

def handleSubmit(request):
    if request.method == 'POST':
        # Get the post parameters
        report_id = request.POST['reportid']
        case_type = request.POST['casetype']
        location = request.POST['loc']
        pin_code = request.POST['pin']
        details = request.POST['details']

        # Create user
        case = Report(reportid=report_id,case_type=case_type,loc = location, pincode=pin_code, case_details=details)
        case.save(Report)
        return HttpResponse('ENTERED DETAILS HAS SUCCESSFULL SAVED')
    else:
        return HttpsResponse('404-Not Found')
