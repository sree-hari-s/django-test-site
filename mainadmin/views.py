from django.shortcuts import render,redirect
from .models import AdminInfo
from django.db import connection
from django.views.decorators.cache import cache_control
from passlib.hash import pbkdf2_sha256
from django.contrib.auth.models import User

@cache_control(no_cache = True,must_revalidate = True,no_store = True)
def admin_login(request):
    if request.method == 'POST':
        admin=AdminInfo.objects.all()
        password_1=request.POST['password']
        username1=request.POST['name']
        for val in admin:
            user_name=val.username
            password_2=val.password
        if password_1==password_2 and user_name==username1 :
            request.session["is_logged_in"]=True
            return redirect('admin_home')
        else:
            msg="Invalid username or password"
            return render(request,'admin_login.html',{'message':msg})       
    elif 'is_logged_in' in request.session:
        return redirect('admin_home')
    else:
        return render(request,'admin_login.html')
    
def index(request):          
    return render(request,'admin.html')
        

@cache_control(no_cache = True,must_revalidate = True,no_store = True)
def logout(request):
    if 'is_logged_in' in request.session:
        del request.session['is_logged_in']
        return redirect('admin_login')
    else:
        return redirect('admin_login')
    

@cache_control(no_cache = True,must_revalidate = True,no_store = True)
def show_users(request):
    #show all users in a table
    if 'is_logged_in' in request.session:
        users=User.objects.all()
        return render(request,'Users.html',{"users":users})
    else:
        return redirect('admin_login')
    
@cache_control(no_cache = True,must_revalidate = True,no_store = True)
def edit_user(request,id):  
    #edit user in database 
    if 'is_logged_in' in request.session:
        user=User.objects.get(id=id)
        if request.method == "POST":
            user_data=User.objects.filter(id=id).all()
            user_name=request.POST['username']
            email=request.POST['email']
            # password1=request.POST['password']
            # eny_password=pbkdf2_sha256.encrypt(password1,rounds=12000,salt_size=32)
            for user in user_data:
                user.email=email
                user.username=user_name
                # if len(password1)<12:
                #     user.password = eny_password
                user.save()
            return redirect('user_admin_home')
        else:
            return render(request,'edit_user_form.html',{'user':user})
    else:
        return redirect('admin_login')  
        
        
@cache_control(no_cache = True,must_revalidate = True,no_store = True)
def delete_user(request,id):
    #delete user in database
    if 'is_logged_in' in request.session:
        the_user=User.objects.filter(id=id).all()
        the_user.delete()
        return redirect('user_admin_home')
    else:
        return redirect('admin_login')

def searched_user(request):
    #for searching user in database
    if request.method == 'POST':
        data=request.POST['searched_data']
        user_data=User.objects.filter(username__contains=data).all()
        if user_data :
            return render(request,'user_searched_data.html',{'user_data':user_data,'data1':data})
        else:
            msg="No data found"
            return render(request,'user_searched_data.html',{'m':msg})