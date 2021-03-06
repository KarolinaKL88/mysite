"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from polls.views import hello
urlpatterns = [
    # path('accounts/login/', LoginView.as_view(), name='login'), #dodane nowe - do logowania
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('polls/', include('polls.urls')),
    path('polls/', include('polls.class_urls')),
    path('polls/', include('polls.generic_urls')),
    path('movies/', include('movies.urls')),
    path('movies/', include('movies.class_urls')),
    path('movies/', include('movies.generic_urls')),
    path('accounts/', include('accounts.urls'))
]
