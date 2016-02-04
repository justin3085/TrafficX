from django.contrib import admin
from complaintlog.models import Complaint
# Register your models here.

class ComplaintAdmin(admin.ModelAdmin):
    model = Complaint
    list_display = ('complaintType', 'street', 'description',)
    prepopulated_fields = {'slug': ('complaintType',)}





admin.site.register(Complaint, ComplaintAdmin)