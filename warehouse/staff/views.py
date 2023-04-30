from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import StaffModel
from .forms import StaffFormAdmin, StaffFormUser
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
        form = StaffFormAdmin(request.POST)
        if form.is_valid():
            messages.success(request, "Account Created")
            form.save()
            return redirect("all-staff")
    form = StaffFormAdmin()
    return render(
        request, "staff/register.html", {"form": form, "title": "GRM Register"}
    )


def update_by_admin(request, pk):
    """update profile by admin - with most of the fields"""
    user = get_object_or_404(klass=StaffModel, pk=pk)
    form = StaffFormAdmin(instance=user)
    if request.method == "POST":
        form = StaffFormAdmin(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated!")
            return redirect("main-page")
    return render(
        request, "staff/update.html", {"form": form, "title": "GRM User update"}
    )


def update_by_user(request, pk):
    """update profile by user - just some fields"""
    user = get_object_or_404(klass=StaffModel, pk=pk)
    form = StaffFormUser(instance=user)
    if request.method == "POST":
        form = StaffFormUser(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated!")
            return redirect("main-page")
    return render(
        request, "staff/update.html", {"form": form, "title": "GRM User update"}
    )


def delete_user(request, pk):
    """delete user"""
    user_to_delete = get_object_or_404(klass=StaffModel, pk=pk)
    if request.method == "POST":
        user_to_delete.delete()
        messages.info(request, "User deleted!")
        return redirect("all-staff")
    return render(
        request,
        "staff/delete.html",
        {"title": "GRM User delete", "user": user_to_delete},
    )


def all_staff(request):
    """all rescuers from rescue group"""
    staff = StaffModel.objects.all()
    return render(
        request, "staff/staff-all.html", {"staff": staff, "title": "GRM People"}
    )
