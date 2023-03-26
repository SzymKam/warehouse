from django.urls import path
from .views import (
    ContainerDelete,
    ContainerUpdate,
    ContainerCreate,
    ContainerView,
    ContainerDetail,
)
from .views import warehouse_main


urlpatterns = [
    path("", warehouse_main, name="warehouse-main"),
    path("containers/", ContainerView.as_view(), name="containers-home"),
    path("containers/<int:pk>", ContainerDetail.as_view(), name="containers-detail"),
    path(
        "containers/update/<int:pk>",
        ContainerUpdate.as_view(),
        name="containers-update",
    ),
    path("containers/create", ContainerCreate.as_view(), name="containers-create"),
    path(
        "containers/delete/<int:pk>",
        ContainerDelete.as_view(),
        name="containers-delete",
    ),
]
