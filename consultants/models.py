from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class Job(models.Model):
  id = models.AutoField(primary_key=True)
  job_name = models.CharField(max_length=50)
  job_type = models.CharField(max_length=50)
  def __str__(self):
    return self.job_name

class Consultant(models.Model):
  user = models.OneToOneField(User, related_name='consultant', on_delete=models.CASCADE, primary_key=True)
  job = models.ForeignKey(Job, on_delete=models.DO_NOTHING, default='')
  job_industry = models.CharField(max_length=50)
  job_experience = models.IntegerField(default=3)
  linkedin = models.CharField(max_length=200, blank=True)
  phone = models.CharField(max_length=20, blank=True)
  description = models.TextField(blank=True)
  join_date = models.DateTimeField(default=datetime.now, blank=True)
  photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
  rating = models.IntegerField(default=0)
  totalsession = models.IntegerField(default=0)
  is_mvp = models.BooleanField(default=False)
  is_online = models.BooleanField(default=False)
  def __str__(self): 
    return self.user.first_name + ' ' + self.user.last_name