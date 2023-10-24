from django.urls import path
from staff.views.reset_password import (
    MyPasswordResetView,
    MyPasswordResetDoneView,
    MyPasswordResetCompleteView,
    MyPasswordResetConfirmView,
)
from staff.views.staff_management import (
    StaffRegister,
    StaffLogin,
    StaffLogout,
    StaffUpdate,
    StaffDelete,
    AllStaff,
)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = (
    [
        path("login/", StaffLogin.as_view(), name="login"),
        path("logout/", StaffLogout.as_view(), name="logout"),
        path("register/", StaffRegister.register, name="register"),
        path("update/<int:pk>", StaffUpdate.update_by_user, name="update"),
        path("update/admin/<int:pk>", StaffUpdate.update_by_admin, name="admin-update"),
        path("delete/<int:pk>", StaffDelete.delete_user, name="delete-user"),
        path("", AllStaff.as_view(), name="all-staff"),
        path("reset_password/", MyPasswordResetView.as_view(), name="reset-password"),
        path(
            "reset_password_sent/",
            MyPasswordResetDoneView.as_view(),
            name="password_reset_done",
        ),
        path(
            "reset/<uidb64>/<token>",
            MyPasswordResetConfirmView.as_view(),
            name="password_reset_confirm",
        ),
        path(
            "reset_password_complete/",
            MyPasswordResetCompleteView.as_view(),
            name="password_reset_complete",
        ),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
