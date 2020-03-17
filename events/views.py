from django.shortcuts import render, redirect,get_object_or_404
from .models import Event
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage


def home(request):
    context = {
        'events': Event.objects.all()
    }
    return render(request, 'events/home.html', context)


def about(request):
    return render(request, 'events/about.html', {'title': 'about'})


def details(request, id=None):
    instance = get_object_or_404(Event, id=id)
    context ={

        "event": instance
    }
    return render(request, "events/details.html", context)



