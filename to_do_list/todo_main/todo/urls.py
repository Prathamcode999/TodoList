from django.urls import path
from . import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'), #this url actually will not be seen openig in seach bar instead in seen action where we have inserted the url in add button.
    #but then will the url open new page for this ? ans: its redirecting to the same webpage again added through views.
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    path('mark_as_undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:pk>', views.delete_task, name='delete_task'),
]