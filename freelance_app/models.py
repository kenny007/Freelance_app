from django.db import models

# Create your models here.
class JobListing(models.Model):
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

