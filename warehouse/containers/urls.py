from django.urls import path, include

# from .views import ContainerDetailView, ContainerListView, ContainerDetailView
from .views import container_list, container_detail


urlpatterns = [
    # path('', ContainerListView.as_view(), name='containers-home'),
    # path('<int:pk>/', ContainerDetailView.as_view(), name='containers-detail'),
    path("", container_list, name="containers-home"),
    path("<int:pk>", container_detail, name="containers-detail"),
]
