from django.db import models
from author.models import Author
# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateField()
    genre = models.CharField(max_length=40)
    author = models.ForeignKey(   
        Author, 
        on_delete= models.CASCADE,
        related_name = 'libs'
    )