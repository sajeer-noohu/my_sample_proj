from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class BaseUser(models.Model):
    user = models.OneToOneField(User, unique=True)
    def __unicode__(self):
        return self.user.username 
    
class Author(BaseUser):
    STATUS = {'active':1, 'inactive':0}
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    
    
    status = models.IntegerField(choices=[(v, k) for k,v in STATUS.items()], default='active', db_index=True)
    
    tweets_count = models.IntegerField(blank=True, null=True, default=0)
    created_on = models.DateTimeField(default=datetime.now)
    updated_on = models.DateTimeField(auto_now=True)
    photo = models.CharField(max_length=255, null=True, blank=True)
    
    
class Editor(BaseUser):
    STATUS = {'active':1, 'inactive':0}

    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(choices=[(v, k) for k,v in STATUS.items()], default=STATUS['active'], db_index=True)
    created_on = models.DateTimeField(default=datetime.now)
    updated_on = models.DateTimeField(auto_now=True)
    photo = models.CharField(max_length=255, null=True, blank=True)