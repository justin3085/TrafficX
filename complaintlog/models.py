from django.db import models

# Create your models here.
class Complaint(models.Model):

    complaintType = models.CharField(max_length=25, verbose_name="Complaint Type")
    dateofcomplaint = models.DateField(verbose_name="Date of Complaint")
    street = models.CharField(max_length=100, verbose_name="Street")
    xstreet = models.CharField(max_length=100, verbose_name="Cross Street", blank=True)
    description = models.TextField(verbose_name="Description")
    slug = models.SlugField(unique=True)