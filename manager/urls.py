from django.urls import path
from . import views
urlpatterns = [
    path('mangerlogin/',views.AdminLogin,name='mangerlogin'),
    path('',views.home,name='home'),
    path('logout/',views.LogOut,name='LogOut')
    
]