from django.forms import ModelForm
from complaintlog.models import Complaint
from django import forms

class ComplaintForm(ModelForm):
    class Meta:
        model = Complaint
        fields = ('complaintType', 'description', 'fname', 'lname', 'street','date_of_complaint',)


# class ComplaintForm(forms.ModelForm):
#     class Meta:
#         model = Complaint
#         COMPLAINT_TYPES_CHOICES = (
#             ('----','----'),
#             ('Speeding', 'Speeding'),
#             ('Parking', 'Parking'),
#             ('Sign Request', 'Sign Request'),
#             ('Survey', 'Survey'),
#
#
#         )
#         fields = ('fname','complaint_type',)
#         complaint_type = forms.ChoiceField(choices=COMPLAINT_TYPES_CHOICES)

        def __init__(self, *args, **kwargs):
            super(ComplaintForm, self).__init__(*args, **kwargs)
            self.fields['complaint_type'].label = "Select Complaint Type "

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)


    #make it more personal
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email"
        self.fields['content'].label = "What do you want to say?"