from django.urls import path
from .views import GetAllContainers, GetContainer, CreateContainer, DeleteContainer

urlpatterns = [
    path("containers/", GetAllContainers.as_view(), name="get-all-containers"),
    path("containers/<int:pk>/", GetContainer.as_view(), name="get-container"),
    path("containers/create/", CreateContainer.as_view(), name="create-container"),
    path(
        "containers/delete/<int:pk>", DeleteContainer.as_view(), name="delete-container"
    ),
]
