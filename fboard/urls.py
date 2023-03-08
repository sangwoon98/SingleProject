from django.urls import path
from . import views

app_name = "fboard"

urlpatterns = [
    path("<int:nowpage>/f_list/", views.f_list, name="f_list"),
    path("<int:nowpage>/<int:f_No>/f_delete/", views.f_delete, name="f_delete"),
    path("<int:nowpage>/<int:f_No>/f_modify/", views.f_modify, name="f_modify"),
    path("<int:nowpage>/<int:f_No>/f_view/", views.f_view, name="f_view"),
    path("<int:nowpage>/<int:f_No>/f_reply/", views.f_reply, name="f_reply"),
    path("<int:nowpage>/f_write/", views.f_write, name="f_write"),
    path("low_comment/", views.low_comment, name="low_comment"),
    path("low_comment_write/", views.low_comment_write, name="low_comment_write"),
    path("f_event/", views.f_event, name="f_event"),
    # path('<int:post_id>/comments/create/',views.comments_create,name='conments_create'), id, comment/create
]
