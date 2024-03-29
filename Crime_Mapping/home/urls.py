from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
   path("",views.index,name='home'),
   path("about",views.about,name='about'),
   path('signup',views.handleSignup,name='handleSignup'),
   path('login',views.handleLogin,name='handleLogin'),
   path('logout',views.handleLogout,name='handleLogout'),
   path('submit',views.handleSubmit,name='handleSubmit'),
   path('map',views.map,name='map'),
]