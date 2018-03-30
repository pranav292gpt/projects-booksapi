from __future__ import unicode_literals

from django.db import models
from db.models import User

SEARCH_ENDPOINT_CHOICES = (
        ("Book" , "Book"),
        ("TV", "TV"),
        ("Movie", "Model"),
        ("Song", "Song"),
        ("General", "General")
        )

class Search(models.Model):
    user = models.ForeignKey(User, related_name="searches")
    request = models.TextField()
    response = models.TextField()
