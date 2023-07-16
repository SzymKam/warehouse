from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required()
def main_page(request):
    """main page of app"""
    return render(
        request,
        "containers/main-page.html",
        {"title": "GRM Main Page", "subtitle": "Main page"},
    )
