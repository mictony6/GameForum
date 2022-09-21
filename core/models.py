from pyexpat import model
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='01')
    description = models.TextField(blank=True, null=True)
    images = models.ImageField()

    def get_absolute_url(self):
        return reverse("post", kwargs={"pk": self.pk})
