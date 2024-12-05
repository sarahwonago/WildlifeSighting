from rest_framework import viewsets, filters

from django_filters.rest_framework import DjangoFilterBackend


from .models import Report
from .serializers import ReportSerializer

class ReportViewSet(viewsets.ModelViewSet):
    """
    Viewset for managing wildlife reports.
    """

    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = [
        "status",
        "animal_type"
    ]
    search_fields = [
        "description",
        "animal_type"
    ]
    ordering_fields = [
        "created_at",
        "updated_at"
    ]
    ordering = [
        "-created_at"
    ]
