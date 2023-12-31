from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from .models import Todo
from .forms import TodoModelForm

class TodoList(ListView):
    queryset = Todo.objects.all()
    template_name = "todolist.html"

class IndivTodo(DetailView):
    template_name = "indivtodo.html"

    def get_object(self, queryset=Todo.objects.all()):
        print(self.kwargs)
        pk = self.kwargs.get("pk")
        print(pk)
        return Todo.objects.get(id=pk)

class MakeNotify(CreateView):
    form_class = TodoModelForm
    template_name = "makenotify.html"

# Create your views here.
