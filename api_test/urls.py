"""django_vue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.conf.urls import url, include
from .views import *


urlpatterns = [
    url(r'add_book', add_book),
    url(r'show_books$', show_books),
    url(r'del_book', del_book),
    url(r'search_book/', search_book),
    url(r'look_delete/', look_delete),
    url(r'token', make_token),
    url(r'register', register),
    url(r'login', login)

]

# (?P<id>\w+)
