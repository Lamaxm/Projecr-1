from django.urls import path
from . import views


app_name = "shawer_app"

urlpatterns = [
    path("all/", views.list_consultant, name="list_consultant"),
    path("comment/all/<pk>", views.comment_list, name="list_comment"),
    path("delete/<comment_id>", views.delete_comment, name="delete_comment"),
    path("comment/add/", views.add_comment, name="add_comment"),
    path("time/add/", views.add_time, name="Add_time"),
    path("course/add/", views.add_course, name="add_course"),
    path("courses/delete/<course_id>", views.delete_course, name="delete_course"),
    path("courses/update/<course_id>", views.update_courses, name="update_courses"),
]