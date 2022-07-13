from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Permission
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from main.forms import SignUpForm


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
        data['button'] = 'Login'
        return data


login_ = Login.as_view()


class IsAdmin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_superuser


class Home(CustomLoginRequiredMixin, IsAdmin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = 'Home'
        data['header'] = 'Home'
        permission = Permission.objects.get(codename='add_object')
        print(self.request.user.has_perm(permission))
        # self.request.user.user_permissions.remove(permission)
        # self.request.user.user_permissions.add(permission)
        # print(self.request.user.user_permissions.all())
        return data


home_ = Home.as_view()


class Logout(LogoutView):
    next_page = reverse_lazy('LOGIN')


logout_ = Logout.as_view()


class ChangePassword(PasswordChangeView):
    template_name = 'login.html'
    success_url = reverse_lazy('LOGIN')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = "Change Password"
        data['header'] = 'Change Password'
        data['button'] = 'Change Password'
        return data


change_password_ = ChangePassword.as_view()


class ResetPassword(PasswordResetView):
    template_name = 'login.html'
    email_template_name = 'email_temp.html'
    success_url = reverse_lazy('LOGIN')
    from_email = 'reset@djangoapp.com'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = "Reset Password"
        data['header'] = 'Reset Password'
        data['button'] = 'Send Email'
        return data


reset_passwd = ResetPassword.as_view()


class PasswordResetDone(PasswordResetDoneView):
    template_name = 'password_reset_done.html'


passwd_reset_done = PasswordResetDone.as_view()


class ConfirmPasswordReset(PasswordResetConfirmView):
    template_name = 'reset_confirm.html'
    success_url = reverse_lazy('LOGIN')


confirm_reset_passwd = ConfirmPasswordReset.as_view()


class SignUp(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("LOGIN")
    template_name = "login.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = "SignUp"
        data['header'] = 'SignUp'
        data['button'] = 'SignUp'
        return data

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.is_superuser = True
        self.object.save()
        return response


sign_up = SignUp.as_view()
