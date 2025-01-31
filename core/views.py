# core/views.py

from django.shortcuts import redirect, render
from .models import UserProfile, Todo
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

def index(request):
    return redirect("tasks/")

def get_user_todos(user: UserProfile) -> list[Todo]:
    return user.todos.all().order_by("created_at")

@login_required
@require_http_methods(["GET", "POST"])
def tasks(request):
    if request.method == "POST":
        return _create_todo(request)
    
    context = {
        "todos": get_user_todos(request.user),
        "fullname": request.user.get_full_name() or request.user.username,
    }

    return render(request, "tasks.html", context)

@login_required
@require_http_methods(["PUT"])
def toggle_todo(request, task_id):
    todo = request.user.todos.get(id=task_id)
    todo.is_completed = not todo.is_completed
    todo.save()

    return render(request, "tasks.html#todo-item-partial", {"todo": todo})


def _create_todo(request):
    title = request.POST.get("title")
    if not title:
        raise ValueError("Title is required")

    todo = Todo.objects.create(title=title, user=request.user)
    return render(request, "tasks.html#todo-item-partial", {"todo": todo})

