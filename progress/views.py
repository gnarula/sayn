from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from progress.forms import RegistrationForm
from progress.models import CustomUser, Society

# Create your views here.

def index(request):
    return render(request, 'progress/index.html')

def login(request):
    # if user is logged in then redirect to the dashboard

    if request.method == "POST":
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(email=email, password=password)
        if user is not None and user.is_active:
            # Login the user
            auth.login(request, user)
            return JsonResponse({'message': 'Login Successful'}, status=200)
        else:
            return JsonResponse({'message': 'Invalid Username/Password'}, status=500)
    return render(request, 'progress/login.html')

def dashboard(request):
    return render(request, 'progress/dashboard.html')

def newuser(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            # Save the User
            form.save()
            return HttpResponseRedirect('/dashboard', {'success', 'User Created Successfully'})
        else:
            return render(request, 'progress/newuser.html', {'form': form})
    else:
        form = RegistrationForm
        return render(request,'progress/newuser.html', {'form': form})
