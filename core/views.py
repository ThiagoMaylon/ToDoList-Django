from django.views.generic import ListView
from .models import Tarefa

class TarefaList(ListView):
    model = Tarefa
    template_name = 'index.html'
    context_object_name = 'tarefas'
    