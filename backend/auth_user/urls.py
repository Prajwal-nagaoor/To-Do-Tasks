from django.urls import path
from . import views
urlpatterns = [
    path('reg', views.register),
    path('login', views.login_),
    path('logout', views.logout_),
]