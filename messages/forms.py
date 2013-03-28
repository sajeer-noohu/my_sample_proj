from django import forms
from django.forms.widgets import Widget

class TweetForm(forms.Form):
    tweet_message = forms.CharField(required=True, help_text='Tweet message', widget=forms.Textarea(attrs={'cols':0, 'rows':0}))
    

    def clean(self):
        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super(TweetForm, self).__init__(*args, **kwargs)
    