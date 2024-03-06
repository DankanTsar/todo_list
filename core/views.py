from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import ToDoItem
from .forms import ToDoForm


class ToDoListView(ListView):
    model = ToDoItem
    template_name = 'todo_list.html'  # change this to your own template


class ToDoCreateView(CreateView):
    model = ToDoItem
    form_class = ToDoForm
    template_name = 'add_todo.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('listtodo')


class ToDoUpdateView(UpdateView):
    model = ToDoItem
    form_class = ToDoForm
    template_name = 'update_todo.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('listtodo')


class ToDoDeleteView(DeleteView):
    model = ToDoItem
    template_name = 'delete_todo.html'

    def delete(self, request, *args, **kwargs):
        # object = self.get_object()
        # if object.created_by != request.user:
        #     raise PermissionDenied  # import this from django.core.exceptions
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('listtodo')