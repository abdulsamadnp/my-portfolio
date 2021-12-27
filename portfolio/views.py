from django.shortcuts import render
from .models import Project
from portfolio.form import ContactMeForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages


def home(request):
    projects = Project.objects.all()
    return render(request, "home.html", {"projects": projects})



def mhome(request):
    form = ContactMeForm()

    if request.method == 'POST':
        form = ContactMeForm(request.POST)
        if form.is_valid():
            # form.save()
            # send_mail(subject, message[fname, lname, email, phonenumber, subject, message], sedner, recipient)

            subject = "Contact form inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name':form.cleaned_data['last_name'],
                'email': form.cleaned_data['emailid'],
                'phonenumber': form.cleaned_data['phone_number'],
                'subject': form.cleaned_data['subject'],
                'message': form.cleaned_data['message'],
            }

            message = '\n'.join(body.values())

            sender = form.cleaned_data['emailid']
            recipient = ['samadchalad@gmail.com']

            try:
                send_mail(subject, message, sender, recipient, fail_silently=True)

            except BadHeaderError:
                return HttpResponse("Invalid header found.")

            messages.success(request, "Your respoce has been submited successfully")
    context = {
        'form':form,
    }
    return render(request, "home.html", context)