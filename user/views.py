from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from user.forms import RegisterForm
# Create your views here.


class UserCreateView(CreateView):
    form_class = RegisterForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy('login')
