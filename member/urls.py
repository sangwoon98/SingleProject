from . import views
from django.urls import path

app_name = 'member'
urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('register02', views.register02, name='register02'),
    path('register03', views.register03, name='register03'),
    path('register04', views.register04, name='register04'),
    path('check_id', views.check_id, name='check_id'),
]
