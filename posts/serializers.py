from rest_framework import serializers
from .models import postModel, tagModel, commentModel


class tagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = tagModel
        fields = "__all__"


class commentSerializer(serializers.ModelSerializer):
    class Meta:
        model = commentModel
        fields = "__all__"


class postSerializers(serializers.ModelSerializer):
    class Meta:
        model = postModel
        fields = "__all__"
        depth = 1


class postSerializersPOST(serializers.ModelSerializer):
    class Meta:
        model = postModel
        fields = "__all__"
