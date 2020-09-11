from django.urls import path
from . import views

urlpatterns =[
    path('task/',views.task,name='task'),
    path('table/',views.table,name='table'),
    path('ok2/',views.new_task),
    path('register/',views.register,name='register'),
    path('delete/<str:pk>/',views.deleteTask,name='delete'),

]
