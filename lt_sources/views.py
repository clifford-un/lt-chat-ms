from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Chat
from .serializers import ChatSerializer

class ChatView(APIView):

    def get(self, request):
        serializer = ChatSerializer(Chat.objects.all(), many=True)
        response = {"Chats": serializer.data}
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = request.data
        serializer = ChatSerializer(data=data)
        if serializer.is_valid():
            chat = Chat(**data)
            chat.save()
            response = serializer.data
            return Response(response, status=status.HTTP_200_OK)