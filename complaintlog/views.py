from django.shortcuts import render
from complaintlog.models import Complaint
# Create your views here.
def index(request):
    complaints = Complaint.objects.all()

    return render(request, 'index.html', {
        'complaints':complaints


    })