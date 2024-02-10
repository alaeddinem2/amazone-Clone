from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.generate_code import generate_code
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,related_name = "user_profile",on_delete = models.CASCADE)
    image = models.ImageField(upload_to='profile',null=True,blank=True)
    code = models.CharField(max_length=10,default=generate_code)

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created :
        Profile.objects.create(
            user = instance
        )


ADDRESS_TYPE = (
    ('Home', 'Home'),
    ('Bussiness', 'Bussiness'),
    ('Office', 'Office'),
    ('Academy', 'Academy'),
    ('Other', 'Other'),
    
)

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name = "user_address")
    type = models.CharField(max_length=10, choices= ADDRESS_TYPE)
    address = models.TextField(max_length = 50)
    notes = models.TextField(null = True, blank = True)

PHONE_TYPE = (
    ('Home', 'Home'),
    ('Bussiness', 'Bussiness'),
    ('Office', 'Office'),
    ('Academy', 'Academy'),
    ('Other', 'Other'),
    
)

class Phone(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name = "user_phone")
    type = models.CharField(max_length=10, choices= PHONE_TYPE)
    phone = models.CharField(max_length=14)
    activate_code = models.CharField(max_length=8,default= generate_code)

    