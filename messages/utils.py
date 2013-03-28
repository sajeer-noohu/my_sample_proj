#from messages.models import DirtyWords

def get_dirty_words():
#    return DirtyWords.objects.all()
    return [(10, 'dirty1'), (20, 'dirt y2'), (30, 'dirty 3'), (40, 'dirty')]

    
def validate_tweet_message(message=None):
    if message:
        import re
        cleaned_message = re.sub(r'[^a-zA-Z0-9]', '', message).lower()
        dirty_words =  get_dirty_words()
        for word_id, word in dirty_words:
            word =  word.lower().replace(' ', '')
            if word in cleaned_message:
                return word_id, False
        return  0, True
     
    return 0, False

def get_words_to_replace(self):
#    return WordsToReplace.objects.all()
    return [(10, 'word1', 'QBurst1'), (20, 'word 2', 'QBurst2'), (30, 'word', 'QBurst3')]