from django.shortcuts import render

def user_login(request):
    return render(request, 'login.html')


def user_signup(request):
    username= request.POST.get("username")
    pwd = request.POST.get("password")
    name = request.POST.get('name')
    
    if username is None or pwd is None or name is None:
        msg1 = "Bad request..! All field are required"
        return render(request, 'signup.html', {'msg':msg1})
    
def home(reqeust):
    
    pass