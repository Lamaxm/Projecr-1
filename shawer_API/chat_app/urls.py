from django.urls import path
from . import views
urlpatterns = [

    path('messages/<int:sender>/<int:receiver>', views.message_list, name='message_detail'),
    path('messages/', views.message_list, name='message_list'),
    path('users/<int:pk>', views.user_list, name='user_detail'),
    path('users/', views.user_list, name='user_list')

]