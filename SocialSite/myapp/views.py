from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

# Create your views here.
from myapp import forms


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "myapp/signup.html"
