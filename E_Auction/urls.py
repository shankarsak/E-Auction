"""E_Auction URL Configuration

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
from django.urls import path
from E_Auction import views     #importviews
from django.contrib.auth import views as auth_views
from users import views as user_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainHome, name="main_home"), 
    path('aboutus/', views.aboutUs, name="about"),     #aboutus
    path('random/<random>', views.random, name=""),  #for random urls
    path('contact/', views.contact, name="contact"),
    path('register/', user_views.register, name="register"),
    #path('login/', views.login, name="login"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
  #  path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
