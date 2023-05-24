from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    StaffRegister,
    StaffLogin,
    StaffLogout,
    StaffUpdate,
    StaffDelete,
    AllStaff,
)
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("login/", StaffLogin.as_view(), name="login"),
    path("logout/", StaffLogout.as_view(), name="logout"),
    path("register/", login_required(StaffRegister.register), name="register"),
    path("update/<int:pk>", login_required(StaffUpdate.update_by_user), name="update"),
    path(
        "update/admin/<int:pk>",
        login_required(StaffUpdate.update_by_admin),
        name="admin-update",
    ),
    path(
        "delete/<int:pk>", login_required(StaffDelete.delete_user), name="delete-user"
    ),
    path("", login_required(AllStaff.as_view()), name="all-staff"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
