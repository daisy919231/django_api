from django.db import models

# Create your models here.

class Author(models.Model):
    first_name=models.CharField(100)
    last_name=models.CharField(100)

class Book(models.Model):
    title=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    author=models.ForeignKey( Author,on_delete=models.CASCADE, related_name='books')
    published_at=models.DateTimeField(auto_now_add=True)
    
