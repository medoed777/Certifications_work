from django.urls import path, include
from rest_framework.routers import DefaultRouter
from network.views import SupplierViewSet, NetworkNodeViewSet

router = DefaultRouter()


router.register(r'suppliers', SupplierViewSet)
router.register(r'network-nodes', NetworkNodeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]