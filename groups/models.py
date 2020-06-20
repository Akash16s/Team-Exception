from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class groupModel(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=255, null=True, blank=True)
    users = models.ManyToManyField(get_user_model())
    image = models.ImageField(upload_to='groups/', null=True, blank=True)

    def __str__(self):
        return self.title
