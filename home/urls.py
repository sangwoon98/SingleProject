from . import views
from django.urls import path

app_name = 'home'
urlpatterns = [
    path('',views.home,name='home'),
    path('top', views.top, name='top'),
    # path('web_admin', views.web_admin, name='web_admin'),
]
