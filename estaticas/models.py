from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone = PhoneNumberField()
    contact_reason = models.CharField(max_length=100)
    description = models.TextField(max_length=460,null=False,blank=True)
    solved = models.BooleanField(default=False, null=False, blank = False)
    mod_comments = models.TextField(max_length=520, default='')