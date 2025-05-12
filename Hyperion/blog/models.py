from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    signature = models.CharField(max_length=140, default="Aspire to have no desire")
    date = models.DateTimeField()
    
    def __str__(self):
        return self.title
    