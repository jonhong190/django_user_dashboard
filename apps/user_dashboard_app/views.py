from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request,'user_dashboard_app/index.html')

def sign_in(request):
    return render(request, 'user_dashboard_app/sign_in.html')


