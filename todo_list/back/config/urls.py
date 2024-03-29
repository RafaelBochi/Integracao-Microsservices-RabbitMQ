from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from app.views import ListViewSet
from usuario.router import router as usuario_router

router = DefaultRouter()
router.register(r"lists", ListViewSet)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/", include(usuario_router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
