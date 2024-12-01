from django.urls import path, include
from .views import ContactsViewSet, check_email
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'contacts', ContactsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('check-email/', check_email, name='check-email'),
]