from django.contrib import admin
from complaintlog.models import Complaint
#from complaintlog.models import Social
# Register your models here.


class ComplaintAdmin(admin.ModelAdmin):

    model = Complaint
    list_display = ('complaintType', 'street', 'description',)
    prepopulated_fields = {'slug': ('street','complaintType','lname', 'date_of_complaint')}

    def __unicode__(self):
        return self.complaintType


# class SocialAdmin(admin.ModelAdmin):
#     model = Social
#     list_display = ('network', 'username',)
#
#
#
# admin.site.register(Social,SocialAdmin)
admin.site.register(Complaint, ComplaintAdmin)

