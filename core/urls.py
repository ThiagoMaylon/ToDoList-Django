from django.contrib import admin
from django.urls import path

from .views import TarefaList

urlpatterns = [
    path('', TarefaList.as_view(), name='index')
]
