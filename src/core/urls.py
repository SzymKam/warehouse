from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .env import env


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("containers.urls")),
    path("staff/", include("staff.urls")),
    path("api/", include("api.urls")),
]

handler403 = "containers.views.error_403.error_403"


if env("DEBUG"):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
