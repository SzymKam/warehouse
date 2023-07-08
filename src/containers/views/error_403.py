from django.shortcuts import render


def error_403(request, exception):
    return render(request, "containers/403.html")
