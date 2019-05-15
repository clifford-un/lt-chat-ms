from django.db import models
from mongoengine import Document, fields

class Chat(Document):
    chat_user_origin = fields.IntField(required=True)
    chat_group_destination = fields.IntField(required=True)
    chat_text = fields.StringField(requiered=True)
    chat_date_stamp=fields.DateTimeField(required=False)