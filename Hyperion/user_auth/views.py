
# Imports for views.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm
from django.contrib import messages


def register(request):
    """
    Handles user registration by receiving HttpRequest. 
    Returns HttpResponse by displaying register.html or redirects to polls index page.
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('polls:index')
    else:
        form = RegisterForm()
    return render(request, 'authentication/register.html', {'form': form})


def login_user(request):
    """
    Handles user login by receiving HttpRequest.
    Returns HttpResponse by displaying login.html or redirects to register or the polls index.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('polls:index')
        else:
            messages.error(request, "Invalid username or password. Please register before logging in.")
            return redirect('user_auth:register')
    return render(request, 'authentication/login.html')

