from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Complaint(models.Model):

    COMPLAINT_TYPES = (
        ('Speeding','Speeding'),
        ('Parking','Parking'),
        ('Sign Request','Sign Request'),
        ('Survey','Survey'),
        ('View Obstruction','View Obstruction'),
        ('Engineering','Engineering'),
        ('General','General'),
        ('Stop Sign', 'Stop Sign'),

    )
    fname = models.CharField(max_length=100, verbose_name="First Name", blank=True, null=True)
    lname = models.CharField(max_length=100, verbose_name="Last Name", blank=True, null=True)
    address = models.CharField(max_length=100, verbose_name="Address", blank=True, null=True)
    phone = models.IntegerField(verbose_name="Phone Number", blank=True, null=True)
    altphone = models.IntegerField(verbose_name="Alt. Phone", blank=True, null=True)
    email = models.EmailField(verbose_name="Email", blank=True,null=True)
    city = models.CharField(max_length=100, verbose_name="City", blank=True, null=True)
    date_of_complaint = models.DateField(verbose_name="Date of Complaint", null=True)
    complaintType = models.CharField(max_length=25, choices=COMPLAINT_TYPES, verbose_name="Complaint Type", null=True)
    street = models.CharField(max_length=100, verbose_name="Street")
    xstreet = models.CharField(max_length=100, verbose_name="Cross Street", blank=True, null=True)
    description = models.TextField(verbose_name="Description", null=True)
    slug = models.SlugField(unique=True)


    #user = models.ForeignKey(to=Band, related_name="members", null=True, blank=True)

    def __unicode__(self):
        return self.complaintType


class ComplaintActivity(models.Model):
    pass





