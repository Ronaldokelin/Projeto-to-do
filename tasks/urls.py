from tasks.views import taskList
from django.urls import path
 
from . import views

from django.urls.conf import include
from django.urls import include, path


urlpatterns = [
    path('helloworld/', views.helloworld), 
    path('', views.taskList, name="task-list"),
    path('task/<int:id>', views.taskView, name='task-view'),
    path('yourname/<str:name>', views.yourName, name='your-name'),
    
]
