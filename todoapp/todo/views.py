from django.shortcuts import render
from .models import todo
# Create your views here.
def todos(request):
    todos = todo.objects.all()

    return render(request, 'todos.html', {'todos': todos})
