from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .models import Chat
from .serializers import ChatSerializer

class ChatView(APIView):

    def get(self, request, format=None):
        response = {'message': 'test by Dia Kurosawa'}
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = request.data
        serializer = ChatSerializer(data=data)
        if serializer.is_valid():
            chat = Chat(**data)
            chat.save()
            response = serializer.data
            return Response(response, status=status.HTTP_201_CREATED)

class ChatViewDetail(APIView):

    def get_object(self, chat_room_id):
        try:
            return Chat.objects.filter(chat_room_id=chat_room_id, chat_hidden = False)
        except Chat.DoesNotExist:
            raise Http404

    def get(self, request,chat_room_id, format=None):
        serializer = ChatSerializer(self.get_object(chat_room_id), many=True)
        response = serializer.data
        return Response(response, status=status.HTTP_200_OK)

class ChatViewDelete(APIView):

    def get_object(self, id):
        try:
            return Chat.objects.get(id=id)
        except Chat.DoesNotExist:
            raise Http404
    
    def delete(self, request, id, format=None):
        chat = self.get_object(id)
        chat.chat_hidden=True
        chat.save(update_fields=['chat_hidden'])
        response = 'mensaje eliminado'
        return Response(response, status=status.HTTP_204_NO_CONTENT) 


    

