from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . models import Task

# Create your views here.
def addTask(request):
    createtask = request.POST['task_added'] #task_added is the name attribute in html page under input tag 
    Task.objects.create(task=createtask)
    return redirect('home')

def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk) #when we click the mark as done option it opens the description wrt its primary key
    task.is_completed = True
    task.save()
    # return HttpResponse(task)
    return redirect('home')

def mark_as_undone(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')
   
def edit_task(request,pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task_added'] # task is name attribute in input tag
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task':get_task,
        }
        return render(request, 'edit.html', context)
    
def delete_task(request,pk):
    task = get_object_or_404(Task, pk = pk)
    task.delete()
    return redirect('home')