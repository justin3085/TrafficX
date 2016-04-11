from django.contrib import admin
from complaintlog.models import Complaint

# Register your models here.
class ComplaintAdmin(admin.ModelAdmin):

    model = Complaint
    list_display = ('complaintType', 'street', 'description','lname',)
    prepopulated_fields = {'slug': ('street','complaintType','lname', 'date_of_complaint')}

    def __unicode__(self):
        return self.complaintType

class ComplaintActivityAdmin(admin.ModelAdmin):
    pass



# class SocialAdmin(admin.ModelAdmin):
#     model = Social
#     list_display = ('network', 'username',)


#admin.site.register(Social,SocialAdmin)
admin.site.register(Complaint, ComplaintAdmin)


