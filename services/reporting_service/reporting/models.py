import uuid
from django.db import models

class Report(models.Model):
    """
    Model representing a wildlife sighting report.
    """

    REPORT_STATUS = [
        ("Pending", "Pending"),
        ("Resolved", "Resolved"),
        ("Escalated", "Escalated")
    ]

    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    animal_type = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    photo_url = models.URLField(
        blank=True,
        null=True
    )
    status = models.CharField(
        max_length=50,
        choices=REPORT_STATUS,
        default="Pending"
        
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.animal_type} sighted at {self.location}"
