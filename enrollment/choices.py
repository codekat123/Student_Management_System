from django.db import models



class EnrollmentStatus(models.TextChoices):
    ACTIVE = "ACTIVE", "Active"
    COMPLETED = "COMPLETED", "Completed"
    DROPPED = "DROPPED", "Dropped"
