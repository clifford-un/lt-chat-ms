from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('chats/', views.ChatView.as_view()),
    path('chats/<str:chat_room_id>/', views.ChatViewDetail.as_view()),
    path('chats/<str:id>/', views.ChatViewDelete.as_view()),
]