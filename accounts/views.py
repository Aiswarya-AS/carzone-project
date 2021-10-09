from django.shortcuts import redirect, render
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import Contact
from django.contrib.auth.decorators import login_required
# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password  = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"you are now logged in.")
            return redirect('dashboard')
        else:
            messages.error(request,"Invalid login credentials")
            return redirect('login')
    return render(request,'accounts/login.html')


def register(request):
    #getting user inputs
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        #check if both passwords are same
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username already exists")
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.error(request,"Email already exists")
                return redirect('register')
            else:
                user  = User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)

                #auto login
                auth.login(request,user)
                messages.success(request,"You are now logged in")
                return redirect('dashboard')

                user.save()
                messages.success(request,"You are registered succesfully")
                return redirect('login')
        else:
            messages.error(request,"Password do not match")
            return redirect('register')

    else:
        return render(request,'accounts/register.html')



def logout(request):
    if request.method == 'POST':
        auth.logout(request)
       
        return redirect('home')
    return redirect('home')

@login_required(login_url = 'login')
def dashboard(request):
    user_inquiry = Contact.objects.order_by('-create_date').filter(user_id = request.user.id)
    return render(request,'accounts/dashboard.html',{
        'inquiries':user_inquiry,
    })