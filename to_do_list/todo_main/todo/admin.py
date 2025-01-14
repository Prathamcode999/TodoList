from django.contrib import admin
from todo.models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_completed', 'updated_at') # this tell that you want to see the description and time of updation in list form in admin panel
    search_fields = ('task',) #this allows you to add a search file while searching for descrition field(task)

admin.site.register(Task, TaskAdmin)

 