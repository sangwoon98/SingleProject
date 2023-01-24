from . import views
from django.urls import path

app_name = 'mypage'
urlpatterns = [
    path('mypage', views.mypage, name='mypage'),
    path('change', views.change, name='change'),
    path('get_leave', views.get_leave, name='get_leave'),
    path('coupon', views.coupon, name='coupon'),
    path('pw_change', views.pw_change, name='pw_change'),
]