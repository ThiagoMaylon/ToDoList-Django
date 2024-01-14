from django.views.generic import ListView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .models import Tarefa

class TarefaList(ListView):
    model = Tarefa
    template_name = 'index.html'
    context_object_name = 'tarefas'

class TarefaDeleteList(DeleteView):
    model = Tarefa
    success_url = reverse_lazy('index')
    template_name = 'index.html'
    context_object_name = 'tarefa'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())