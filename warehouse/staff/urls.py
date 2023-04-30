from django.urls import path
from .views import (
    all_staff,
    register,
    StaffLogin,
    StaffLogout,
    update_by_admin,
    update_by_user,
    delete_user,
)

urlpatterns = [
    path("login/", StaffLogin.as_view(), name="login"),
    path("logout/", StaffLogout.as_view(), name="logout"),
    path("register/", register, name="register"),
    path("update/<int:pk>", update_by_user, name="update"),
    path("update/admin/<int:pk>", update_by_admin, name="admin-update"),
    path("delete/<int:pk>", delete_user, name="delete-user"),
    path("", all_staff, name="all-staff"),
]
