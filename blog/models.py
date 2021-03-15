from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# import content_editor
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    # content = models.TextField()
    content = RichTextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={"pk": self.pk })

# test content_editor
class DemoPost(models.Model):
    content = RichTextField()
    


