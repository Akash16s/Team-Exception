from django.contrib.auth import get_user_model
from django.db import models
from posts.models import tagModel


# Create your models here.
class compModel(models.Model):
    topic = models.CharField(max_length=500, blank=False, null=False)
    date = models.DateField(null=False)
    time = models.TimeField(null=False)
    Tags = models.ManyToManyField(tagModel)
    image = models.ImageField(upload_to='comp/', null=True, blank=True)
    desc = models.TextField(blank=True)
    link = models.TextField(blank=False)
    contact = models.TextField(blank=False)
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.topic
