from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class CustomLoginRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy('LOGIN')


class Login(LoginView):
    template_name = 'login.html'


login_ = Login.as_view()


class Home(CustomLoginRequiredMixin, TemplateView):
    template_name = 'index.html'


home_ = Home.as_view()


class Logout(LogoutView):
    next_page = reverse_lazy('LOGIN')


logout_ = Logout.as_view()
