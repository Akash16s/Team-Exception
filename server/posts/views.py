import os
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .serializers import postSerializers, tagsSerializer, commentSerializer
from .models import postModel, tagModel, commentModel
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return ["title", "postType", "parentId", "author", "comment", "tags", "groups"]


class postHandler(generics.ListCreateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = postSerializers
    filter_backends = [DjangoFilterBackend, DynamicSearchFilter]
    filterset_fields = ["title", "postType", "parentId", "author", "tags", "score", "groups"]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return postModel.objects.order_by("-pk")

    @staticmethod
    def chackSentiment(data, title):
        key = os.getenv("TEXT_KEY")
        endpoint = "https://hackjaipur.cognitiveservices.azure.com/"
        credential_ta = AzureKeyCredential(key)
        text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, credential=credential_ta)
        response = text_analytics_client.analyze_sentiment(documents=[data, title])
        return response

    def post(self, request, *args, **kwargs):
        sentiment = self.chackSentiment(request.data['body'], request.data['title'])
        if sentiment[0]['sentiment'] == 'negative' and sentiment[0]['confidence_scores']['negative'] >= 0.10 or \
                sentiment[1]['sentiment'] == 'negative' and sentiment[1]['confidence_scores']['negative'] >= 0.10:
            return Response({"msg": "Your post doesn't follow the guideline"}, status=400)
        serial = postSerializers(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.validated_data, status=200)
        return Response(serial.errors, status=400)


class tagHandler(generics.ListCreateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = tagsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["tag"]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return tagModel.objects.order_by("-pk")


class commentHandler(generics.ListCreateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = commentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["message", "postId"]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return commentModel.objects.order_by("-pk")
