from rest_framework import serializers
from .models import groupModel


class groupsSerializer(serializers.ModelSerializer):

    class Meta:
        model = groupModel
        fields = "__all__"


class groupsSerializerPut(serializers.ModelSerializer):
    users = serializers.JSONField()

    class Meta:
        model = groupModel
        fields = "__all__"
