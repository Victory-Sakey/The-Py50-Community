from django.shortcuts import render

def Onboarding(request):
    return render(request, 'onboarding.html') 

def Home(request):
    return render(request , 'home.html')

def about(request):
    return render(request , 'about.html')

def join_community(request):
    return render(request , 'jc.html')