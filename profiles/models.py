from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Profile(models.Model):

    profile_name = models.CharField(_("Nom du profil"), max_length=50)
    firstname = models.CharField(_("Prénom"), max_length=255)
    lastname = models.CharField(_("Nom"), max_length=255)
    birthdate = models.DateField(_("Date de naissance"), auto_now=False)
    birthplace = models.CharField(_("Lieu de naissance"), max_length=255)
    address = models.CharField(_("Adresse"), max_length=2047)
    city = models.CharField(_("Ville"), max_length=255)
    zipcode = models.CharField(_("Code postal"), max_length=255)

    def __str__(self):
        return self.profile_name

    def __repr__(self):
        return f"<Profile {self.profile_name}"
