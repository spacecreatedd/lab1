from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return f'{self.user.username}'




class Post(models.Model):
    expiration_time = models.DateTimeField()
    short_description = models.CharField(max_length=200)
    full_description = models.TextField()
    image = models.ImageField(upload_to='media/')
    def is_expired(self):
        return timezone.now() > self.expiration_time

class Choice(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    vote_count = models.IntegerField(default=0)
    voted_users = models.ManyToManyField(User, related_name='voted_choices', blank=True)