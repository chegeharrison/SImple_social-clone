from django.views.generic import TemplateView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms
# Create your views here.
class SignUp (CreateView):
    form_class = forms.UserCreationForm
    success_url =reverse_lazy('login')
    template_name = 'registration/signup.html'

class LogIn(CreateView):
    template_name ='registration/login.html'


