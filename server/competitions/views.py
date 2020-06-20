from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from .serializers import compSerializer
from .models import compModel


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return ["topic", "date", "time", "Tags", "contact"]


# Create your views here.
class compView(generics.ListCreateAPIView):
    serializer_class = compSerializer
    filter_backends = [DjangoFilterBackend, DynamicSearchFilter]
    filterset_fields = ["topic", "date", "time", "Tags", "contact", "user"]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return compModel.objects.order_by("-pk")
