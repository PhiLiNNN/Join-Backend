from django.urls import path, include
from .views import ContactsViewSet, check_email, BoardViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'contacts', ContactsViewSet)
router.register(r'tasks', BoardViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('check-email/', check_email, name='check-email'),
]




