from django.shortcuts import render, redirect


# Create your views here.

def register(requests):
    return render(requests, 'accounts/register.jinja2')


def login(requests):
    return render(requests, 'accounts/login.jinja2')


def logout(requests):
    return redirect(requests, 'index.jinja2')


def dashboard(requests):
    return render(requests, 'accounts/dashboard.jinja2')
