from django.shortcuts import render, redirect
from complaintlog.models import Complaint
from complaintlog.forms import ComplaintForm
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.http import Http404
from complaintlog.forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from complaintlog.models import Complainant


# Create your views here.
def index(request):
    complaints = Complaint.objects.all()

    return render(request, 'index.html', {
        'complaints':complaints

    })

def complaint_detail(request, slug):
    # grab the object
    complaint = Complaint.objects.get(slug=slug)
    #pass to template
    return render(request, 'complaints/complaint_detail.html', {
        'complaint':complaint,
    })

@login_required
def edit_complaint(request, slug):
    complaint = Complaint.objects.get(slug=slug)
    if complaint.complainant != request.complainant:
        raise Http404
    
    form_class = ComplaintForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=complaint)
        if form.is_valid():
            form.save()
            return redirect('complaint_detail', slug=complaint.slug)
    else:
        form = form_class(instance=complaint)
    return render(request, 'complaints/edit_complaint.html', {
            'complaint': complaint,
            'form':form,
        })

def create_complaint(request):
    form_class = ComplaintForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            #complaint.complainant = request.complainant
            complaint.slug = slugify(complaint.complaintType)
            complaint.save()
            return redirect('complaint_detail', slug=complaint.slug)
    else:
        form = form_class()
        return render(request, 'complaints/create_complaint.html', {
            'form':form,
            })

def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            form_content = form.cleaned_data['content']

            template = get_template('contact_template.txt')

            context = Context({
                'contact_name':contact_name,
                'contact_email':contact_email,
                'form_content':form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                'New contact form submission',
                content,
                'Your website <hi@weddinglovely.com>',
                ['jgp3085@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact')

        return render(request, 'contact.html', {
            'form': form_class,
        })

    return render(request, 'contact.html', {
        'form':form_class,
    })