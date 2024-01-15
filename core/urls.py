from django.contrib import admin
from django.urls import path

from .views import TarefaList, TarefaDeleteList, TarefaCreateList

urlpatterns = [
    path('', TarefaList.as_view(), name='index'),
    path('tarefa/delete/<int:pk>', TarefaDeleteList.as_view(), name='delete'),
    path('tarefa/create/', TarefaCreateList.as_view(), name='create')
]
