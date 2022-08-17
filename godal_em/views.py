from django.shortcuts import render, redirect
from accounts.forms import CustomUserChangeForm
from .models import Meter, Request
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RequestForm
# Create your views here.
from random import randint


def uniqueId(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def index(request):
    return render(request, 'pages/index.html')

@login_required
def request_meter(request):
    if request.method == 'POST':
        user_form = CustomUserChangeForm(data=request.POST, files=request.FILES)
        if user_form.is_valid():
            user_form.save()
            Meter.objects.create(
                user = request.user,
                meter_id = uniqueId(8),
            ).save()
            user_form.save()
            messages.success(request, 'Your request have been sent, you will be notified once its approved.')
            return redirect("/")
        else:
            messages.error(request, 'Invalid data Entry, check and try again.')
    else:
        user_form = CustomUserChangeForm()
    
    return render(request, 'pages/request_meter.html', {
        'user_form': user_form,
    })

def buy_power(request):
    if request.method == "POST":
        form = RequestForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            power_form = form.save(commit=False)
            power_form.by = request.user
            power_form.save()
            messages.success(request, 'Request Sent. please standby')
            return redirect("/")
        else:
            messages.error(request, 'Invalid data Entry, check and try again.')
    else:
        user_form = RequestForm()
    
    return render(request, 'pages/buy_power.html', {
        'user_form': user_form,
    })

def secrete_route(request):
    return render(request, 'pages/dashboard.html')

def users(request):
    meters = Meter.objects.all()
    return render(request, 'pages/meters.html', {
        "meters": meters
    })

def power_requests(request):
    requests = Request.objects.all()
    return render(request, 'pages/requets.html', {
        "requests": requests
    })
