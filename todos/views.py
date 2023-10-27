from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from .models import Todo

# Create your views here.


class TodoListView(ListView):
    model = Todo
    paginate_by = 15
    
    def get_queryset(self):
        
        search = self.request.GET.get("title")

        if search:

            todo = Todo.objects.filter(title__icontains=search)
        
        else:
            todo = Todo.objects.all()

        return todo


class TodoCreateView(CreateView):
    model = Todo
    fields = ["title","deadline"]
    success_url = reverse_lazy("todo_list")

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title","deadline"]
    success_url = reverse_lazy("todo_list")

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")

class TodoCompleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.mark_has_complete()
        return redirect("todo_list")
    
