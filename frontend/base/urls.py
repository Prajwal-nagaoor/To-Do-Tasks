from django.urls import path
from . import views
urlpatterns = [
    path('home/<int:pk>/', views.home, name='home'),
    path('add_task/<int:pk>/', views.add_task, name='add_task'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete_, name='delete'),
    path('restore/<int:pk>/', views.restore, name='restore'),
    path('History/<int:pk>/', views.history, name='history'),
    path('delete_all', views.delete_all, name='delete_all'),
    path('restore_all', views.restore_all, name='restore_all'),
    path('del_hist/<int:pk>/', views.del_hist, name='del_hist'),
    path('completed_task/<int:pk>/', views.completed_task, name='completed_task'),
    path('completed_page/<int:pk>/', views.completed_page, name='completed_page'),
]