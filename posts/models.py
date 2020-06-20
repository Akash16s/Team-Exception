import django
from django.db import models
from django.contrib.auth import get_user_model
from groups.models import groupModel


class tagModel(models.Model):
    tag = models.CharField(max_length=255, blank=False, primary_key=True, unique=True)

    def __str__(self):
        return self.tag


# Create your models here.
class postModel(models.Model):
    title = models.TextField(blank=False, max_length=500, null=False)
    postType = models.CharField(max_length=255)
    parentId = models.CharField(blank=True, null=True, max_length=255)
    creationDate = models.DateTimeField(null=False, default=django.utils.timezone.now)
    score = models.IntegerField(default=0)
    body = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    author = models.ForeignKey(get_user_model(), null=True, blank=True, on_delete=models.CASCADE)
    answerCount = models.IntegerField(default=0)
    commentCount = models.IntegerField(default=0)
    closedDate = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField(tagModel, null=True, blank=True)
    groups = models.ManyToManyField(groupModel, null=True, blank=True)

    def __str__(self):
        return self.title


class commentModel(models.Model):
    message = models.TextField(blank=False)
    postId = models.ForeignKey(postModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.message
