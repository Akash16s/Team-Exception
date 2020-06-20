from django.core.exceptions import ObjectDoesNotExist
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .serializers import groupsSerializer, groupsSerializerPut
from .models import groupModel


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return ["title", "description", "users"]


class groupsHandler(generics.ListCreateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = groupsSerializer
    filter_backends = [DjangoFilterBackend, DynamicSearchFilter]
    filterset_fields = ["title", "description", "users"]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return groupModel.objects.order_by("-pk")

    @staticmethod
    def put(request):
        try:
            model = groupModel.objects.get(pk=request.data["id"])
        except ObjectDoesNotExist:
            return Response({"msg": "The id not provided"}, status=400)
        serializer = groupsSerializerPut(model, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data, status=200)
        return Response(serializer.errors, status=400)
