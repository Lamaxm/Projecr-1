from django.urls import path
from . import views


app_name = "user_app"
urlpatterns = [
    path("user/add", views.add_user, name="Add_user"),
    path("update/<user_id>", views.update_user, name="update_user"),
    path("delete/<user_id>", views.delete_user, name="delete_user"),
    path("login", views.login_user, name="login"),
]