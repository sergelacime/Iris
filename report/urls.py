"""Iris URL Configuration

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
from django.urls import re_path,include
from . import views,chatview

urlpatterns = [
    # re_path("$",views.home2, name="Acceuil"),
    re_path("$",views.newR, name="NewR"),
    re_path("NewRep/",views.NewRep, name="NewRep"),
    # re_path("fonction-report/", views.fonction_report, name="fonction-report"),
    re_path('chat/', chatview.chat_view, name='chat'),
    re_path(r'^(?P<id>[0-9]+)/chatOld/', chatview.chat_view_old, name='chatOld'),
    

]
