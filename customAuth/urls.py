"""customAuth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_, name='LOGIN'),
    path('home', home_, name='home'),
    path('logout', logout_, name='LOGOUT'),
    path('update/passwd', change_password_, name='change-password'),
    path('reset/passwd', reset_passwd, name='reset-password'),
    path('reset/passwd/done/<str:uidb64>/<str:token>', confirm_reset_passwd, name='password_reset_confirm'),
]
