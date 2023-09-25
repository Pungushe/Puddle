from django import forms

from . models import СonversationMessage

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = СonversationMessage
        fields = ('content',)

        widgets={
            'content': forms.Textarea(attrs={
                'class': 'w-full px-6 py-4 rounded-xl border'
            })
        }