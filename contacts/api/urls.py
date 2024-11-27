from django.urls import path, include
from .views import ContactsViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'contacts', ContactsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]