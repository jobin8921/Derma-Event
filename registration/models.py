from django.db import models


class Registration(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    registered_at = models.DateTimeField(auto_now_add=True)  # Add this field



