from django.shortcuts import render, redirect
from apps.users.models import User
from django.contrib.auth import authenticate, login
from apps.settings.models import Settings
from django.http.response import HttpResponse
# Create your views here.

def register(request):
    setting = Settings.objects.latest('id')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            user = User.objects.create(username = username, email= email)
            user.set_password(password)
            user.save()
            user = User.objects.get(username = username)
            user = authenticate(username = username, password = password)
            login(request, user)
        return redirect('index')
    context = {
        'setting':setting
    }
    return render(request, 'signup.html', context)

def user_login(request):
    setting = Settings.objects.latest('id')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username)
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('index')
        except:
            return HttpResponse('Неправильный логин или пароль')
    context = {
        'setting':setting
    }
    return render(request, 'login.html', context)