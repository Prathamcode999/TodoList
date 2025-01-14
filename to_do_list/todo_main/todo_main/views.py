from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed = False).order_by('-updated_at') #we filter the task which are not completed in tasks
    completed_tasks = Task.objects.filter(is_completed = True)
    print(completed_tasks)
    context = {
        'taskbar': tasks, # we store all those filetered tasks in taskbar so that we can run loop and access it in html page
        'completed': completed_tasks
    }
    return render(request, 'home.html', context)

 
