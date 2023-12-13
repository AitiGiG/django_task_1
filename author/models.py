from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=40)
    age = models.DateField(auto_now_add=True)
    alias = models.CharField(max_length=40)
    def __str__(self) -> str:
        return f'{self.name}'