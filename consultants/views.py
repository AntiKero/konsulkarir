from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver    
from django.shortcuts import render, redirect
from consultants.models import Consultant, Job


@receiver(user_logged_in)
def got_online(sender, user, request, **kwargs):    
    user.profile.is_online = True
    user.profile.save()

@receiver(user_logged_out)
def got_offline(sender, user, request, **kwargs):   
    user.profile.is_online = False
    user.profile.save()
