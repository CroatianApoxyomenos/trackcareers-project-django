from django import forms

from subscribe.models import Subscribe


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ['first_name', 'last_name', 'email', 'option']

