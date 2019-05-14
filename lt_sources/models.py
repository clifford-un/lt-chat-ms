from django.db import models
from mongoengine import Document, fields

class Chat(Document):
    chat_message = fields.StringField(required=True)
    chat_cal = fields.IntField(required=True)