from django.shortcuts import redirect, render
from .models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate

def user_signup(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password:
           
            hashed_password = make_password(password)
            user = User(username=username, password=password)  
            return redirect('login')  # Redirect to login after signup
        else:
            return render(request, 'signup.html', {'msg': "All fields are required"})
    return render(request, 'signup.html')

   
def user_login(request):
    if 'username' in request.session and request.session['username'] is not None:
            return redirect('home')
    if request.method=='POST':
        username= request.POST.get("username")
        password = request.POST.get("password")
        name = request.POST.get('name')
        user = authenticate(username=username,password=password)
        if user is not None:
            
            return redirect('home')
        else:
            return render(request, 'login.html',{'msg':"Invalid Username or Password"} )
        
    return render(request, 'login.html')
        
 
def home(request):
    if 'username' in request.session:
        msg = f'Welcome {request.session['username']} to Homepage'
        return render(request, 'home.html',{'msg':msg})
    return redirect('user_login')
        
