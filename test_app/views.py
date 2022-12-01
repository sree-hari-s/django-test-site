from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth,User
from django.contrib.auth.hashers import check_password
from django.views.decorators.cache import cache_control
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView,DetailView

# Create your views here.

@cache_control(no_cache = True,must_revalidate = True,no_store = True)
def base(request):
    #Login Page
    if 'user_username' in request.session:
        return redirect('home')
    
    if request.method=="POST":
        login_username=request.POST['username']
        login_password=request.POST['password']
        try:
            check_username=User.objects.filter(username=login_username).get()
        except:
            check_username=None       
        if check_username:
            if check_password(login_password,check_username.password):
                request.session['user_username']=login_username
                return redirect('home')
            else:
                msg="Invalid Username or Password"
                return render(request,'test_app/base.html',{'msg':msg})  
        else:
            msg="Invalid Username or Password"    
            return render(request,'test_app/base.html',{'msg':msg})
        
    return render(request,'test_app/base.html')   

@cache_control(no_cache = True,must_revalidate = True,no_store = True)
def register(request):
    #Register Page
    if request.method=='POST':
        reg_username=request.POST['username']
        reg_email=request.POST['email']
        reg_password1=request.POST['password1']
        reg_password2=request.POST['password2']
        if reg_password1==reg_password2:
            if User.objects.filter(username=reg_username).exists():
                print("Username Taken")
            elif User.objects.filter(email=reg_email).exists():
                print("Email Taken")
            else:
                user=User.objects.create_user(username=reg_username,password=reg_password1,email=reg_email)
                user.save()
                print('User Created')
        else:
            print('Password not matching')
        return redirect('base')
    else:
        return render(request,'test_app/register.html')
    
@cache_control(no_cache = True,must_revalidate = True,no_store = True)     
def home(request):
    if not 'user_username' in request.session:
        return redirect('base')
    username=request.session['user_username']
    return render(request,'test_app/home.html',{'username':username})

def logout(request):
    request.session.flush()
    return redirect('base')
