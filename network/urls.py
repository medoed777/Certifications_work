from django.urls import include, path
from rest_framework.routers import DefaultRouter

from network.views import NetworkNodeViewSet, SupplierViewSet

router = DefaultRouter()


router.register(r"suppliers", SupplierViewSet)
router.register(r"network-nodes", NetworkNodeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
