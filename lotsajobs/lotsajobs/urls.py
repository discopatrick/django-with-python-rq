"""lotsajobs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from sftp import views as sftp_views
from jobs import views as jobs_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobs/', jobs_views.jobs_index, name='jobs_index'),
    path('', sftp_views.sftp_index, name='sftp_index'),
]
