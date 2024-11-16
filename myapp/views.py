from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_view(request):
 if request.method == 'POST':
  #handle login
  username = request.POST['username']
  password = request.POST['password']
  #authenticate user
  user = authenticate(username=username, password=password)
  if user is not None:
   login(request, user)
   return redirect('home')
  else:
   return render(request, 'myapp/login.html', {'error': 'Invalid username or password'})
 else:
  return render(request, 'myapp/login.html')
def logout_view(request):
  logout(request)
  return redirect('login')
def home_view(request):
 return render(request, 'myapp/home.html')