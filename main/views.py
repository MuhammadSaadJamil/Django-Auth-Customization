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
    next_page = reverse_lazy('home')
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = "Login"
        data['header'] = 'Login'
        return data


login_ = Login.as_view()


class Home(CustomLoginRequiredMixin, TemplateView):
    template_name = 'index.html'


home_ = Home.as_view()


class Logout(LogoutView):
    next_page = reverse_lazy('LOGIN')


logout_ = Logout.as_view()
