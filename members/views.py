from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout


#redirect and reverse are used to redirect your route to another page 

# Create your views here.

def members(request):
    return render(request, 'home/index.html')

def signup(request):
    errorMessage = ''
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password_1']
        password_2 = request.POST['password_2']

       

        if password == password_2:
            newUser = User.objects.create_user(username, email, password)
            newUser.save()
            return redirect(reverse('signin'))
        else :
            errorMessage = "passwords does not match"

        
    return render(request, 'signup.html', {'error': errorMessage})

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password_1']
        
        print(
            username + password
        )
        #we use authenticate() to check if the user is in our database
        
        isInDb = authenticate(username=username, password=password)
    
        
        print(isInDb)
        
        if isInDb is not None:
            login(request, isInDb)
            return redirect(reverse('members'))
            
            
    return render(request, 'signin.html')

def signout(request):
    logout(request)
    return redirect(reverse('signin'))