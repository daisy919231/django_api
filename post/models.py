from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    p_title=models.CharField(max_length=100, null=True)
    p_body=models.TextField(null=True)
    p_file=models.FileField(null=True, blank=True, upload_to=('posts/'))
    p_created_at=models.DateTimeField(auto_now_add=True)
    p_updated_at=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts' )

