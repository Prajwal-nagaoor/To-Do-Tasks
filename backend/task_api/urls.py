from django.urls import path
from . import views
urlpatterns = [
    path('tasks/<int:pk>/', views.tasks),
    path('history/<int:pk>/', views.history),
    path('update_task/<int:pk>/',views.update_task),
    path('restore/<int:pk>/',views.restore),
    path('delete_all/',views.delete_all),
    path('delete_hist/<int:pk>/',views.del_hist),
    path('completed_task/<int:pk>/',views.completed_task),
    path('completed_page/<int:pk>/',views.completed_page),
]
