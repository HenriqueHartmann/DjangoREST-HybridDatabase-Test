from rest_framework import routers

from backend.core import views

router = routers.DefaultRouter()
router.register("users", views.UserViewSet, basename="user")
router.register("event", views.EventViewSet, basename="event")
