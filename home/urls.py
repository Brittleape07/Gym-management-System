"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addmembers', views.addmembers, name='addmembers'),
    path('members', views.members, name='members'),
    path('delete/<int:member_id>/', views.delete_data, name='deletedata'),
    path('update<int:member_id>/', views.update, name='update'),
    path('login', views.loginpage, name='login'),
    path('register', views.registerpage, name='register'),
    path('logout', views.logoutUser, name='logout'),
    path('equipments', views.equipments, name='equipments'),
    path('deleteeq/<int:equi_id>/', views.eq_delete_data, name='deletedataeq'),
]
