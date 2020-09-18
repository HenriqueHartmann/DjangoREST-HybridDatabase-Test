from rest_framework import routers

from backend.core import views

router = routers.DefaultRouter()
router.register("users", views.UserViewSet, basename="user")
