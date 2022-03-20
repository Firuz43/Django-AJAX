from django.urls import path
from . import views


urlpatterns = [
    path('', views.apiOverView, name='api-ovreview'),
    path('task-list/', views.taskList, name="task-list"),
    path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
    path('task-create/', views.taskCreate, name="task-create"),
    path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
]
