from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(postModel)
admin.site.register(commentModel)
admin.site.register(tagModel)