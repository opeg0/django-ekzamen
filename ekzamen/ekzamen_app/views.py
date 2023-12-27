from django.shortcuts import render
from .forms import UserRegistrationForm, UserAuthenticationForm, PenaltyForm
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from .models import Penalty

# Create your views here.

def index(request):
    return render(request, 'index.html', {'penalty': Penalty.objects.all()})

def register_view(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            try:
                user = user_form.save(commit=False)
                user.set_password(user_form.cleaned_data['password'])
                user.save()
            except IntegrityError:
                return render(request, 'register.html', {'user_form': user_form})
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})

def login_view(request):
    if request.method == 'POST':
        user_form = UserAuthenticationForm(request.POST)
        if user_form.is_valid():
            validate = user_form.cleaned_data
            user = authenticate(request, username=validate['username'], password=validate['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))
                else:
                    return HttpResponse('Аккаунт не активен')
            else:
                return HttpResponse('Логин или пароль не верны')
    else:
        user_form = UserAuthenticationForm()
    return render(request, 'login.html', {'user_form': user_form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def penalty_add(request):
    if request.method == 'POST':
        penalty_form = PenaltyForm(request.POST)
        if penalty_form.is_valid():
            try:
                penalty = penalty_form.save(commit=False)
                penalty.save()
            except IntegrityError:
                return render(request, 'penalty.html', {'penalty_form': penalty_form})
            return HttpResponseRedirect(reverse('index'))
    else:
         penalty_form = PenaltyForm()
    return render(request, 'penalty.html', {'penalty_form': penalty_form})