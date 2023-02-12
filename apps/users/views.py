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
    return render(request, 'users/signup.html', context)

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
            return HttpResponse('<h1>Неправильный логин или пароль</h1>')
    context = {
        'setting':setting
    }
    return render(request, 'users/login.html', context)

def account(request, username):
    setting = Settings.objects.latest('id')
    user = User.objects.get(username = username)
    context = {
        'setting':setting,
        'user':user,
    }
    return render(request, 'users/creator-profile.html', context)

def edit_profile(request, username):
    user = User.objects.get(username = username)
    if request.user != user:
        return redirect('index')
    setting = Settings.objects.latest('id')
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        about_self = request.POST.get('about_self')
        if 'update' in request.POST:
            user.about_self = about_self
            user.username = username
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()
            return redirect('edit_profile', user.username)
        if 'delete' in request.POST:
            user.delete()
            return redirect('register')
        if 'profile_image_update' in request.POST:
            image = request.FILES.get('image')
            user.profile_image = image
            user.save()
            return redirect('edit_profile', user.username)
    context = {
        'setting':setting,
        'user':user,
    }
    return render(request, 'users/creator-profile-edit.html', context)