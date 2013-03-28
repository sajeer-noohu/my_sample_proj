from django.contrib import admin
from messages.models import DirtyWords, WordsToReplace, Tweet

admin.site.register(WordsToReplace)
admin.site.register(DirtyWords)
admin.site.register(Tweet)