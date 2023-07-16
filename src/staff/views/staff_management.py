from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from staff.models import StaffModel
from staff.forms import StaffFormAdmin, StaffFormUser, StaffFormUpdate
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from typing import Any


class StaffLogin(LoginView):
    """page for login into service"""

    template_name = "staff/login.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "GRM Login"
        return context


class StaffLogout(LogoutView):
    """user logout page"""

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "GRM Logout"
        return context


class AllStaff(LoginRequiredMixin, ListView):
    """all rescuers from rescue group"""

    queryset = StaffModel.objects.all()
    template_name = "staff/staff-all.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "GRM People"
        return context


class StaffRegister:
    @staticmethod
    @login_required
    @permission_required("staff.add_staffmodel", login_url="main-page")
    def register(request):
        """page only for admin, where can add new staff person"""
        if request.method == "POST":
            form = StaffFormAdmin(request.POST)
            if form.is_valid():
                user = form.save()
                messages.success(request, "Account Created")

                for group in form.cleaned_data["groups"]:
                    user.groups.add(group)
                return redirect("all-staff")
        form = StaffFormAdmin()
        return render(
            request, "staff/register.html", {"form": form, "title": "GRM Register"}
        )


class StaffUpdate:
    @staticmethod
    @login_required
    @permission_required("staff.change_staffmodel", login_url="main-page")
    def update_by_admin(request, pk: int):
        """update profile by admin - with most of the fields"""
        user = get_object_or_404(klass=StaffModel, pk=pk)
        form = StaffFormUpdate(instance=user)
        if request.method == "POST":
            form = StaffFormUpdate(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, "Profile updated!")
        return render(
            request,
            "staff/update.html",
            {"form": form, "title": "GRM User by admin update"},
        )

    @staticmethod
    @login_required
    def update_by_user(request, pk: int):
        """update profile by user - just some fields"""
        user = get_object_or_404(klass=StaffModel, pk=pk)
        if request.method == "POST":
            form = StaffFormUser(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, "Profile updated!")
        form = StaffFormUser(instance=user)
        return render(
            request, "staff/update.html", {"form": form, "title": "GRM User update"}
        )


class StaffDelete:
    @staticmethod
    @login_required
    @permission_required("staff.delete_staffmodel", login_url="main-page")
    def delete_user(request, pk: int):
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
