from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserForm



# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'user_profile/login.html')



def user_logout(request):
    logout(request)
    messages.info(request, 'You are logged out')
    return redirect('login')

def user_register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            login(request, new_user)
            messages.success(request, f'Вітаємо, {new_user.username}! Реєстрація успішна.')
            return redirect('index')
        else:
            messages.error(request,'Помилка регістрації')
    else:
        form = UserForm()

    return render(request, 'user_profile/register.html')
