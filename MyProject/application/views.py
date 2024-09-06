from django.shortcuts import render, HttpResponse
from application.models import *
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('contact')
        d = request.POST.get('message')
        enquiry = ContactForm(name = a, email = b, contact = c, message = d)
        enquiry.save()

        messages.success(request, "Thanks for Interacting with us......!")
    return render(request, 'index.html')

def contact(request):
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('contact')
        d = request.POST.get('message')
        details = ContactForm(name = a, email = b, contact = c, message = d)
        details.save()

        messages.success(request, "Thanks for Interacting with us........!")
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def blogdetails(request):
    return render(request, 'blog-details.html')