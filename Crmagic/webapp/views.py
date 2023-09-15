from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from .models import Record
# Create your views here.


@login_required(login_url='webapp:login_user')
def home(request):
    records = Record.objects.all()
    return render(request, 'home.html', {'records': records})


def login_user(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('webapp:home')
        print('not here')
        messages.success(request, 'Username or Password is incorrect')
        return render(request, 'login.html')
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('webapp:login_user')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(
                request, "You Have Successfully Registered! Welcome!")
            return redirect('webapp:home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})


@login_required(login_url='webapp:login_user')
def customer_record(request, pk):
    customer_record = Record.objects.get(id=pk)
    return render(request, 'c_record.html', {'customer_record': customer_record})
