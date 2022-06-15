from django.db import models
from django.conf import settings


# Create your models here.
class Post(models.Model):
    title: models.CharField(max_length= 200)
    text: models.TextField()
    author: models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    created_date: models.DateTimeField(auto_now=True)
    pub_date: models.DateTimeField(auto_now=False)
