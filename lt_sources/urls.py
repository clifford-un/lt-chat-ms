from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('/', views.ChatView.as_view()),
    path('chats/<str:chat_room_id>/', views.ChatViewDetail.as_view()),
    path('chat/<str:id>/', views.ChatViewDelete.as_view()),
]