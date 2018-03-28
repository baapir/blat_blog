from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Blat(models.Model):
    text = models.TextField()
    charactor = models.CharField(max_length=100, default='The Boss')
    source = models.URLField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pic = models.ImageField(blank=True)
    pic_url = models.URLField(blank=True)

    def __str__(self):
        return self.text[:50]

    ##def totall_likes(self):
    ##    return self.like_set.count()


class Like(models.Model):
    blat = models.ForeignKey('Blat', on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='writer')
    created_on = models.DateTimeField(auto_now_add=True)
    blat = models.ForeignKey('Blat', on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.text[:50]

    def get_absolute_url(self):
        return reverse('blat_detail_url', kwargs={'pk': self.pk})
