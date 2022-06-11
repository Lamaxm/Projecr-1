from django.urls import path
from . import views


app_name = "shawer_app"

urlpatterns = [
    path("all/", views.list_consultant, name="list_consultant"),
    path("comment/all", views.comment_detile, name="list_comment"),
    path("delete/<comment_id>", views.delete_comment, name="update_comment"),
    path("comment/add/", views.add_comment, name="add_comment"),
]