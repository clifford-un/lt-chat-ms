from django.db import models
from mongoengine import Document, fields
import datetime

class Chat(Document):
    chat_user_origin = fields.IntField(required=True)
    chat_room_id = fields.IntField(required=True)
    chat_text = fields.StringField(requiered=True)
    chat_hidden = fields.BooleanField(default=False)
    chat_date_stamp = fields.DateTimeField(default=datetime.datetime.today)
    
