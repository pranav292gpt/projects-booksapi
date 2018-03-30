from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    psid = models.CharField(max_length=16, primary_key=True)
    first_name = models.CharField(max_length=32, null=True, blank=True)
    last_name = models.CharField(max_length=32, null=True, blank=True)
    gender = models.CharField(max_length= 16, null=True, blank=True)
