from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from consultants.models import Consultant, Job
from listings.models import Listing
from django.urls import reverse
from accounts.forms import EditProfileForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

def register(request):
  if request.method == 'POST':
    # Get form values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Check if passwords match
    if password == password2:
      # Check username
      if User.objects.filter(username=username).exists():
        messages.error(request, 'That username is taken')
        return redirect('register')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'That email is being used')
          return redirect('register')
        else:
          # Looks good
          user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
          # Login after register
          # auth.login(request, user)
          # messages.success(request, 'You are now logged in')
          # return redirect('index')
          user.save()
          messages.success(request, 'You are now registered and can log in')
          return redirect('login')
    else:
      messages.error(request, 'Passwords do not match')
      return redirect('register')
  else:
    return render(request, 'accounts/register.html')

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are now logged in')
      return redirect('index')
    else:
      messages.error(request, 'Invalid credentials')
      return redirect('login')
  else:
    return render(request, 'accounts/login.html')

def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('index')

def dashboard(request):
  user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

  consultant_contacts = Contact.objects.order_by('-contact_date').filter(consultant_id=request.user.id)

  context = {
    'contacts': user_contacts,
    'consultants': consultant_contacts
  }
  return render(request, 'accounts/dashboard.html', context)


def view_profile(request, pk=None):
  if pk:
      user = User.objects.get(pk=pk)
  else:
      user = request.user
  context = {'user': user}

  return render(request, 'accounts/profile.html', context)

def edit_profile(request):
  if request.method == 'POST':
      form = EditProfileForm(request.POST, instance=request.user)

      if form.is_valid():
          form.save()
          return redirect(reverse('accounts:view_profile'))
  else:
      form = EditProfileForm(instance=request.user)
      context = {'form': form}
      return render(request, 'accounts/edit_profile.html', context) 