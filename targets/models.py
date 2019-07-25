from django.db import models
from django.contrib.auth.models import User

class Target(models.Model):
    title = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    latitude = models.IntegerField(default=0)
    longitude = models.IntegerField(default=0)
    area = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
