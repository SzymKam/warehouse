from django.urls import path
from .views import all_staff, register, StaffLogin, StaffLogout, update

urlpatterns = [
    path("login/", StaffLogin.as_view(), name="login"),
    path("logout/", StaffLogout.as_view(), name="logout"),
    path("register/", register, name="register"),
    path("update/<int:pk>", update, name="update"),
    path("", all_staff, name="all-staff"),
]
