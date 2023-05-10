from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


# Create your views here.

@login_required(login_url='mangerlogin')
@user_passes_test(lambda u: u.is_superadmin)
def home(request):
    return render(request,'myapp/Adminhome.html')




def AdminLogin(request):
    if request.user.is_authenticated:
            return redirect('home')

    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['pass']

        user=authenticate(username=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        
        else:
            messages.error(request,'Inavlid Creadentials')
            return redirect('mangerlogin')
        
    return render(request,'myapp/index.html')

def LogOut(request):
    logout(request)
    return redirect('mangerlogin')

        
