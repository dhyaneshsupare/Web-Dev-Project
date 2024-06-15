from django.db import models

# Create your models here.
class Form(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    contact = models.CharField(max_length=10)
    message = models.TextField()

class ContactForm(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    contact = models.CharField(max_length=10)
    message = models.TextField()