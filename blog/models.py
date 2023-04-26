from django.db import models
from django.shortcuts import reverse

# Form -> Model : ModelFoem
class Post(models.Model):
    STATUS_CHOICES = (
        ('pub', 'Published'),
        ('drf', 'Draft')
    )
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('posts_detail', args=[self.id]) #/blog/<int>/
# Create your models here.

