from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from backend.core.router import router as core_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name="token"),
    path('api/refresh_token/', TokenRefreshView.as_view(), name="refresh_token"),
    path('api/', include(core_router.urls))
]
