from django.urls import path, include

# from .views import ContainerDetailView, ContainerListView, ContainerDetailView
from .views import container_list, container_detail, warehouse_main


urlpatterns = [
    # path('', ContainerListView.as_view(), name='containers-home'),
    # path('<int:pk>/', ContainerDetailView.as_view(), name='containers-detail'),
    path("", warehouse_main, name="warehouse-main"),
    path("containers/", container_list, name="containers-home"),
    path("containers/<int:id>", container_detail, name="containers-detail"),
]
