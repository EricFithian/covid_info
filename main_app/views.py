from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def symptoms(request):
    return render(request, 'symptoms.html')

def testing(request):
    return render(request, 'testing.html')

def vaccines(request):
    return render(request, 'vaccines.html')