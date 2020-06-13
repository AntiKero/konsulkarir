from django.db import models
from datetime import datetime
from listings.models import Listing
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class Contact(models.Model):
  id = models.AutoField(primary_key=True)
  listing = models.ForeignKey(Listing, on_delete=models.DO_NOTHING)
  user = models.ForeignKey(User, related_name='user_login', on_delete=models.DO_NOTHING)
  message = models.TextField(blank=True)
  contact_date = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.message