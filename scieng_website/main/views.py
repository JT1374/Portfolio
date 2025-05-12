# Imports.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Project
from django.contrib.auth.decorators import login_required


# All views functions.
def signup_view(request):
    """
    The view for when a user wishes to sign up.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # automatically log the user in
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'main/signup.html', {'form': form})


def login_view(request):
    """
    The view for when users wish to login which displays the login webpage.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})


def logout_view(request):
    """
    The view for the logout page which allows users to logout.
    """
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return render(request, 'main/logout.html')


def home(request):
    """
    The view for the home page which displays the home web page.
    """
    return render(request, 'main/home.html')


def project_list(request):
    """
    The view for the project list page which lists all projects from db. 
    """
    projects = Project.objects.all()
    return render(request, 'main/project_list.html', {'projects': projects})


@login_required
def project_detail(request, project_id):
    """
    The view for when the link for a project in each project is clicked to display
    the project details webpage for that respective project.
    """
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'main/project_detail.html', {'project': project})
