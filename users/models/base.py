from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from polymorphic.models import PolymorphicModel
from .manager import UserManager
from .choices import EgyptGovernorate

class AbstractUser(AbstractBaseUser, PermissionsMixin, PolymorphicModel):
    full_name = models.CharField(max_length=50, blank=True, null=True)
    national_id = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    
    governorate = models.CharField(
        max_length=30,
        choices=EgyptGovernorate.choices,
        blank=True, null=True
    )
    
    location = models.TextField(max_length=400, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'national_id'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def clean(self):
        if not self.national_id.isdigit():
            raise ValueError('national_id must be numeric')
        if len(self.national_id) < 15:
            raise ValueError('national_id must be 15 number')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
     
    def __str__(self):
        return f"{self.full_name or "???"} => {self.national_id}"
    
    class Meta:
        ordering = ['id']