from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, 'personal/about.html')

def contact(request):
    return render(request, 'personal/contact.html')

def projects(request):
    return render(request, 'personal/projects.html')
