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
from django.urls import re_path
from . import views,Audio_chatview

urlpatterns = [
    # re_path("$",views.home, name="home"),
    # re_path("Acceuil/",views.home2, name="Acceuil"),
    re_path("$",views.home2, name="Acceuil"),
    re_path("New/",views.new, name="New"),
    re_path("executer-fonction/", views.executer_fonction, name="executer_fonction"),
    re_path("voir-text/", views.voir_text, name="voir_text"),
    re_path('Audiochat/', Audio_chatview.Audio_chat_view, name='Audiochat'),
    re_path(r'^(?P<id>[0-9]+)/Audio_chatOld/', Audio_chatview.Audio_chat_view_old, name='AudiochatOld'),

]
