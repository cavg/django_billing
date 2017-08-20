from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from billing.models import Plan

# @login_required
def plans(requests):
    plans = Plan.objects.values_list('name', flat=True)
    return HttpResponse(str(list(plans)))