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
    animal_type = models.CharField(
        max_length=255,
        help_text="Type of animal spotted"
        )
    description = models.TextField(help_text="Description of the sighting")
    location = models.CharField(
        max_length=255,
        help_text="Geolocation of the sighting"
        )
    photo_url = models.URLField(
        blank=True,
        null=True,
        help_text="url  of the uploaded photo"
    )
    status = models.CharField(
        max_length=50,
        choices=REPORT_STATUS,
        default="Pending",
        help_text="Current status of the report"
        
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.animal_type} sighted at {self.location}"


# import uuid
# from django.contrib.gis.db import models
# from django.utils.translation import gettext_lazy as _

# class Report(models.Model):
#     """Model to store wildlife reports."""

#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     animal_type = models.CharField(max_length=100, help_text=_("Type of animal spotted"))
#     description = models.TextField(help_text=_("Description of the sighting"))
#     location = models.PointField(help_text=_("Geolocation of the sighting"))
#     photo_url = models.URLField(blank=True, null=True, help_text=_("URL of the uploaded photo"))
#     status = models.CharField(
#         max_length=50,
#         choices=[("PENDING", "Pending"), ("RESOLVED", "Resolved"), ("ESCALATED", "Escalated")],
#         default="PENDING",
#         help_text=_("Current status of the report"),
#     )
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.animal_type} - {self.status}"
