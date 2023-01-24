from . import views
from django.urls import path

app_name = 'event'
urlpatterns = [
    path('event/<int:nowpage>/',views.event,name='event'),
    path('event_view/<int:nowpage>/<int:no>/',views.event_view,name='event_view'),
    # path('event_view_previous/<int:nowpage>/<int:no>',views.event_view_previous,name='event_view_previous'),
    # path('event_view_next/<int:nowpage>/<int:no>',views.event_view_next,name='event_view_next'),
    path('event_reply_write/<int:no>/',views.event_reply_write,name='event_reply_write'),
    path('event_reply_repair/<int:no>/',views.event_reply_repair,name='event_reply_repair'),
    path('event_reply_delete/<int:no>/',views.event_reply_delete,name='event_reply_delete'),
    # path('event_list',views.event_list,name='event_list'),
    # path('web_admin', views.web_admin, name='web_admin'),
]

