"""dashboard URL Configuration

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
from django.views.generic import TemplateView

urlpatterns = [
    # home page
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    # dashboard page
    path(
        'analytical/',
        TemplateView.as_view(template_name='dashboard/analytical.html'),
        name='analytical'
    ),
    # authentication page
    path(
        'login/',
        TemplateView.as_view(template_name='authentication/login.html'),
        name='login'
    ),
    path(
        'register/',
        TemplateView.as_view(template_name='authentication/register.html'),
        name='register'
    ),
    # forms page
    path(
        'form-basic/',
        TemplateView.as_view(template_name='forms/form-layout/form-basic.html'),
        name='form-basic'
    ),
    path(
        'bootstrap-validation/',
        TemplateView.as_view(template_name='forms/form-validation/bootstrap-validation.html'),
        name='bootstrap-validation'
    ),
    path(
        'custom-validation/',
        TemplateView.as_view(template_name='forms/form-validation/custom-validation.html'),
        name='custom-validation'
    ),
    # tables
    path(
        'table-basic/',
        TemplateView.as_view(template_name='tables/bootstrap/table-basic.html'),
        name='table-basic'
    ),
    path(
        'datatable-basic/',
        TemplateView.as_view(template_name='tables/datatables/datatable-basic.html'),
        name='datatable-basic'
    ),
]
