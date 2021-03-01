from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals
# Create your models here.


class Profile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    def __str__(self):
        return f'{self.User.username} profile'

