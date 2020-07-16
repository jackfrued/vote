"""vote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from polls.views import show_subjects, show_teachers, praise_or_criticize, login, register, get_captcha, show_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_index),
    path('api/subjects/', show_subjects),
    path('api/teachers/', show_teachers),
    path('praise/', praise_or_criticize),
    path('criticize/', praise_or_criticize),
    path('login/', login),
    path('register/', register),
    path('captcha/', get_captcha),
]
