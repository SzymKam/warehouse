from django.shortcuts import render
from django.shortcuts import HttpResponse


def error_403(request, exception) -> HttpResponse:
    return render(request, "containers/403.html")
