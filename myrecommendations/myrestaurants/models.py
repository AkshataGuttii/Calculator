from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date

class Restaurant(models.Model):
    Number_first = models.IntegerField(blank=True, null=True)
    Number1_second = models.IntegerField(blank=True, null=True)
    