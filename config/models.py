from django.db import models
from django.utils.translation import gettext_lazy as _ 
# Create your models here.

class company(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    logo = models.ImageField(_("Logo"), upload_to="company")
    subtitle = models.TextField(_("Subtitle"), max_length=500)
    fb_link = models.URLField(_("Facebook "), max_length=200)
    tw_link = models.URLField(_("Twitter"), max_length=200)
    in_link = models.URLField(_("Linkedin"), max_length=200)
    email = models.EmailField(_("Email"), max_length=254)
    phone = models.CharField(_("Phone"), max_length=50)
    address = models.CharField(_("Address"), max_length=50)