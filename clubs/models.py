from django.db import models
from users.models import CustomUser

# Create your models here.

class Club(models.Model):
    users = models.ManyToManyField(CustomUser,related_name='clubs')
    mods = models.ManyToManyField(CustomUser,related_name='mod_clubs')
    
    