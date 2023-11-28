from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.

#def home(request):
#    return HttpResponse("<h1>Welcome to home page</h1>")

def dashboard(request):
    return render(request, 'dashboard.html')

def login_view(request):
    return render(request, 'login.html')

def registration_view(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        my_user = User.objects.create_user(uname,email,pass1)
        my_user.save()

        return redirect('loginview')

        #print(uname,email,pass1,pass2)
    
    return render(request, 'registration.html')

