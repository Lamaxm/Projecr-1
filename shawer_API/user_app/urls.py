from django.urls import path
from . import views


app_name = "user_app"

urlpatterns = [
    path("client/add", views.add_client, name="Add_client"),
    path("consultant/add", views.add_consultant, name="Add_consultant"),
    path("all/", views.list_consultant, name="list_consultant"),
    path("update/<user_id>", views.update_user, name="update_user"),
    path("delete/<user_id>", views.delete_user, name="delete_user"),
]