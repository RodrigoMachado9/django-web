from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def register(requests):
    if requests.method == 'POST':
        print('SUBMITTED REG')
        # Register User
        messages.error(requests, 'Testing error messge')
        return redirect('register')
    return render(requests, 'accounts/register.jinja2')


def login(requests):
    if requests.method == 'POST':
        # Login User
        return redirect('login')
    return render(requests, 'accounts/login.jinja2')


def logout(requests):
    return redirect(requests, 'index.jinja2')


def dashboard(requests):
    return render(requests, 'accounts/dashboard.jinja2')
