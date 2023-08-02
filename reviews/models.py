from django.db import models

# Create your models here.

class Review(models.Model):
    user_name = models.CharField(max_length=100)
    reiview_text = models.TextField(max_length=300)
    rating = models.IntegerField()
    owner_comment = models.TextField(max_length=300)