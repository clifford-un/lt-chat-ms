from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('chats/', views.ChatView.as_view()),
    path('chats/<str:id>/', views.ChatViewDetail.as_view()),
]