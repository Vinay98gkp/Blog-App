from django.contrib import admin
from django.urls import path,include
from core import views

urlpatterns = [
    path('',views.index,name='home'),
    path('index/',views.index),
    path('about/',views.about),
    path('categories/<category>/',views.categories),
    path('contact/',views.contact),
    path('addblog/',views.addblog),
    path("post/<id>/",views.post),
    path('admin/',views.admin),
    path('signin/',views.signin, name='signin'),
    path('signup/',views.signup),
    path('logout/',views.logout),
    path('setting/',views.setting),
    
    
        
    
]