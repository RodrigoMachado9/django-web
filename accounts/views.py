from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth


# Create your views here.


def register(requests):
    if requests.method == 'POST':
        # print('SUBMITTED REG')
        # # Register User
        # messages.error(requests, 'Testing error message')

        # Get form values
        first_name = requests.POST["first_name"]
        last_name = requests.POST["last_name"]
        username = requests.POST["username"]
        email = requests.POST["email"]
        password = requests.POST["password"]
        password2 = requests.POST["password2"]

        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(requests, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(requests, 'That email is being used')
                    return redirect('register')
                else:
                    # Looks good
                    user = User.objects.create_user(username=username, password=password, email=email,
                                                    first_name=first_name, last_name=last_name)
                    # Login after register
                    # auth.login(requests, user)
                    # messages.success(requests, 'You are now logged in')
                    # return redirect('index')
                    user.save()
                    messages.success(requests, 'You are now registered ans can log in')
                    return redirect('login')

            messages.info(requests, 'Successful registration')
            return redirect('index')
        else:
            messages.error(requests, 'Password do not match')
            return redirect('register')
    else:
        return render(requests, 'accounts/register.jinja2')


def login(requests):
    if requests.method == 'POST':
        username = requests.POST["username"]
        password = requests.POST["password"]

        user = auth.authenticate(username=username, password=password)
        # Login User
        if user is not None:
            auth.login(requests, user)
            messages.success(requests, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(requests, 'Invalid credentials')
            return redirect('login')

    return render(requests, 'accounts/login.jinja2')


def logout(requests):
    if requests.method == 'POST':
        auth.logout(requests)
        messages.success(requests, 'You are now logged out')
        return redirect('index')

    return redirect(requests, 'index.jinja2')


def dashboard(requests):
    return render(requests, 'accounts/dashboard.jinja2')
