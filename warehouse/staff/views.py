from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Staff
from .forms import StaffForm
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView


class StaffLogin(LoginView):
    """page for login into service"""

    template_name = "staff/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "GRM Login"
        return context


class StaffLogout(LogoutView):
    """user logout page"""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "GRM Logout"
        return context


def register(request):
    """page only for admin, where can add new staff person"""
    if request.method == "POST":
        form = StaffForm(request.POST)
        if form.is_valid():
            print("User created")
            messages.success(request, "Account Created")
            form.save()
            return redirect("main-page")
    form = StaffForm()
    return render(
        request, "staff/register.html", {"form": form, "title": "GRM Register"}
    )


def update(request, pk):
    """update user profile"""
    user = Staff.objects.filter(pk=pk)
    all = Staff.objects.all()
    return HttpResponse(f"{user} and all: {all}")


def all_staff(request):
    """all rescuers from rescue group"""
    staff = Staff.objects.all()
    return render(
        request, "staff/staff-all.html", {"staff": staff, "title": "GRM People"}
    )
