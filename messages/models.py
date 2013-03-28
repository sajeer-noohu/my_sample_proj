from django.db import models
from users.models import Author  
from messages.utils import get_words_to_replace, get_dirty_words
from django.template.defaultfilters import default

class DirtyWords(models.Model):
    dirty_word = models.CharField(max_length=140, null=False, blank=False)
    
    def __unicode__(self):
        return self.dirty_word

class WordsToReplace(models.Model):
    
    word_to_replace = models.CharField(max_length=140, null=False, blank=False)
    word_replace_with = models.CharField(max_length=140, null=False, blank=False)
    def __unicode__(self):
        return self.word_to_replace

    
class Tweet(models.Model):
    STATUS = {'posted':1, 'not-posted':2}
    
    original_tweet_message = models.CharField(max_length=140, null=False, blank=False)
    formated_tweet_message = models.CharField(max_length=140, null=True, blank=True)
    author = models.ForeignKey(Author, blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    status = models.IntegerField(choices=[(v, k) for k, v in STATUS.items()], blank=False, null=False, default=STATUS['not-posted'])
    first_dirty_word = models.IntegerField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        
        self.formated_tweet_message = self.get_formated_message()
        self.author = Author.objects.all()[1]
        if self.is_valid_message():
            self.tweet_the_message()
        else:
            self.status = self.STATUS['not-posted']

        super(Tweet, self).save(*args, **kwargs)
    
    def is_valid_message(self):
        message = self.original_tweet_message
        if message:
            import re
            cleaned_message = re.sub(r'[^a-zA-Z0-9]', '', message).lower()
            dirty_words =  DirtyWords.objects.select_related().all()
            for word in dirty_words:
                dirty_word =  word.dirty_word.lower().replace(' ', '')
                if dirty_word in cleaned_message:
                    self.first_dirty_word = word.id
                    return False

            return  True
     
        return False

    def get_formated_message(self):
        formated_message = None
        if self.formated_tweet_message:
            formated_message = self.formated_tweet_message
        elif self.original_tweet_message:
            formated_message = self.original_tweet_message
            if formated_message:
                words_to_replace = WordsToReplace.objects.select_related().all()
#                print words_to_replace
                for word in words_to_replace:
                    formated_message = formated_message.replace(word.word_to_replace, word.word_replace_with)

        return formated_message
        
    def tweet_the_message(self):
        
        self.status = self.STATUS['posted']
