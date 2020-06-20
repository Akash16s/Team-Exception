from rest_framework import serializers
from .models import compModel


class compSerializer(serializers.ModelSerializer):
    class Meta:
        model = compModel
        fields = "__all__"
