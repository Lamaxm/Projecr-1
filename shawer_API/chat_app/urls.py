from django.urls import path
from . import views
urlpatterns = [

    path('api/messages/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),
]