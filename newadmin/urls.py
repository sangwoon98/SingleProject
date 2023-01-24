from . import views
from django.urls import path

app_name = 'newadmin'
urlpatterns = [
    path('admin', views.admin, name='admin'),
    path('form', views.form, name='form'),
    path('tabels', views.tabels, name='tabels'),
    
    path('main_list', views.main_list, name='main_list'),
    path('main_write', views.main_write, name='main_write'),
    path('main_top_view/<int:no>', views.main_top_view, name='main_top_view'),
    path('main_top_delete/<int:no>', views.main_top_delete, name='main_top_delete'),
    path('main_multi_delete', views.main_multi_delete, name='main_multi_delete'),

    
    path('event_write', views.event_write, name='event_write'),
    path('event_list/<int:nowpage>', views.event_list, name='event_list'),
    path('event_delete/<int:nowpage>/<int:no>', views.event_delete, name='event_delete'),
    path('event_multi_delete', views.event_multi_delete, name='event_multi_delete'),
    path('event_list_view/<int:nowpage>/<int:event_no>', views.event_list_view, name='event_list_view'),
    
    path('member_list/<int:nowpage>', views.member_list, name='member_list'),
    path('member_multi_delete', views.member_multi_delete, name='member_multi_delete'),
    
    path('community_list/<int:nowpage>', views.community_list, name='community_list'),
    path('community_multi_delete', views.community_multi_delete, name='community_multi_delete'),
]
