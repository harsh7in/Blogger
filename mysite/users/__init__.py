from django.contrib.auth.signals import user_logged_out, user_logged_in
from django.dispatch import receiver
from time import perf_counter
from .models import Profile

log_in_time = 0
log_out_time = 0
total_time_spent = 0

@receiver(user_logged_in)
def log_in(sender, user, request, **kwargs):
  global log_in_time
  log_in_time = perf_counter()

@receiver(user_logged_out)
def log_out(sender, user, request, **kwargs):
  global log_out_time
  log_out_time = perf_counter()
  calculate_total_time(user)

def calculate_total_time(user):
  global log_in_time
  global log_out_time
  global total_time_spent
  total_time_spent = log_out_time - log_in_time
  save_time(total_time_spent, user)

def save_time(total_time_spent, user):
  p = Profile.objects.raw('SELECT user from Profile WHERE user  = %s', [user])
  
  p.save()
