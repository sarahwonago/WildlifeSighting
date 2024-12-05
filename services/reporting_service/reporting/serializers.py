from rest_framework import serializers
from .models import Report

class ReportSerializer(serializers.ModelSerializer):
    """
    Serializer for the animal sight Report model.
    """

    class Meta:
        model = Report
        fields = '__all__'