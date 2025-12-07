from django.urls import path

from . import views

urlpatterns = [
    path('reg',views.register, name='register'),
    path('', views.login_, name='login'),
    path('lgoout', views.logout_, name='logout'),
    path('profile', views.profile, name='profile')
]