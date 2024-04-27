from django.shortcuts import redirect, render
from .models import User

def user_login(request):
    return render(request, 'login.html')


def user_signup(request):
    if request.session['username'] is not None:
        return redirect(home)
    
    username= request.POST.get("username")
    pwd = request.POST.get("password")
    name = request.POST.get('name')
    
    if not (username and pwd and name):
        msg1 = "Bad request..! All field are required"
        return render(request, 'signup.html', {'msg':msg1})
    
    user = User(username=username,password=pwd, name=name)
    user.save()
    return redirect("home")
    
    
def user_login(request):
    if request.method=='POST':
        if request.session['username'] is not None:
            return redirect(home)
        username= request.POST.get("username")
        pwd = request.POST.get("password")
    

        
 
def home(request):
    
    pass
