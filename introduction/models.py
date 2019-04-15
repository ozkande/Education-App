from django.db import models

# Create your models here.

class Message(models.Model):
    student_email = models.CharField(max_length= 100)
    student_subject = models.CharField(max_length=100)
    student_textfield = models.TextField(max_length=500)