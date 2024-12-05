from rest_framework import serializers
from .models import Report

class ReportSerializer(serializers.ModelSerializer):
    """
    Serializer for the animal sight Report model.
    """
    status = serializers.CharField(read_only=True)

    class Meta:
        model = Report
        fields = [
            "animal_type",
            "description",
            "location",
            "photo_url",
            "status"
        ]