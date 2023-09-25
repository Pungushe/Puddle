from django.contrib import admin

from .models import Conversation, СonversationMessage

admin.site.register(Conversation)
admin.site.register(СonversationMessage)