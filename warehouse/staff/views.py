from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect


def login(request):
    return HttpResponse("Login page")


# Create your views here.
