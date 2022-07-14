from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Report
import folium 
import datetime
import geopy
from geopy.geocoders import Nominatim



# Create your views here.


# from django.shortcuts import redirect

# def view_404(request, exception=None):
#     # make a redirect to homepage
#     # you can use the name of url or just the plain link
#     return redirect('/') # or redirect('name-of-index-url')

def error_404_view(request, exception):
    return render(request,'home.html')


def index(request):
    return render(request,'home.html') 

def about(request):
    content={'content':'ABOUT'}
    return render(request,'about.html')


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
            context={'msg':"", 'html': ''}
            return render(request,'login.html',context)
        else:
            messages.error(request,"Invalid Credentials,Please try again")
            return redirect('home')
    else:
        return redirect('home')

def handleLogout(request):
    # content={'content': 'HOME'}
    return render(request, "home.html")
    # return render(request,"home.html",content)

def handleSubmit(request):
    if request.method == 'POST':
        # Get the post parameters
        fir_id = request.POST['fir_id']
        pol_st_ID = request.POST['pol_st_ID'] #changes should be here
        location = request.POST['loc']
        date_tym = request.POST['date_tym']
        if(date_tym==''):
            date_tym=datetime.datetime.now()
        
        details = request.POST['case_detail']
        dhara = request.POST['dhara']
        if(dhara==''):
            dhara='dhara1'

        if(fir_id == '' or  pol_st_ID == '' or location == ''):
            context={'msg':False, 'html': '<div class="alert alert-danger" role="alert">There is some error</div>'}
            return render(request,'login.html',context)

        # location to lat long
        geolocator = Nominatim(user_agent="sudo")
        locate = geolocator.geocode(location)
        print(locate)
        if(locate is None):
            context={'msg':False, 'html': '<div class="alert alert-danger" role="alert">There is some error in finding place</div>'}
            return render(request,'login.html',context)
        lat=locate.latitude
        lon=locate.longitude



        # Create user
        case = Report(Fir_Id=fir_id,Police_St_ID=pol_st_ID,Location = location, Date_Time=date_tym, Case_Details=details,Dhaara=dhara,longitute=lon,latitude=lat)
        case.save(Report)
        context={'msg':True, 'html': '<div class="alert alert-secondary" role="alert">Submitted successfully</div>'}
        return render(request,'login.html',context)
        return HttpResponse('ENTERED DETAILS HAS SUCCESSFULL SAVED')
    else:
        context={'msg':False, 'html': '<div class="alert alert-danger" role="alert">There is some error</div>'}
        return render(request,'login.html',context)
        return HttpsResponse('404-Not Found')


def map(request):
    #create map object
    allreport=Report.objects.all()
    m=folium.Map(location=[20.5937, 78.9629],zoom_start=5)
    
    for report in allreport: 
        d='black'
        if(report.Dhaara=='dhara1'):
             d = 'green'
        if(report.Dhaara=='dhara2'):
             d = 'blue'
        if(report.Dhaara=='dhara3'):
             d = 'orange'
        if(report.Dhaara=='dhara4'):
             d = 'red'
        folium.Marker(
        location=[report.latitude, report.longitute],
        popup=report.Location,
        icon=folium.Icon(color=d, icon="cloud"),
        ).add_to(m)
    
    m=m._repr_html_()

    context={
        'm':m,
    }
    return render(request,'map.html',context)

def analysis(request):
    df = pd.read_csv('C:/Users/ABC/Desktop/Crime/MCI_2014_to_2019.csv',sep=',') 
    major_crime_indicator = df.groupby('MCI',as_index=False).size()
    print(major_crime_indicator)

    plt.subplots(figsize = (15, 6))
    ct = major_crime_indicator.sort_values(ascending = False)
    ax = ct.plot.bar()
    ax.set_xlabel('Offence')
    ax.set_ylabel('Total Number of Criminal Cases from 2014 to 2019')
    ax.set_title('Major Crime Indicator',color = 'red',fontsize=25)
    plt.show()
    context={'ax':ax,}
    return render(request,'analysis.html',context)