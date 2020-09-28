from rest_framework import routers

from backend.core import views

router = routers.DefaultRouter()
router.register("user", views.UserViewSet, basename="user")
router.register("event", views.EventViewSet, basename="event")
router.register("submission", views.SubmissionViewSet, basename="submission")
