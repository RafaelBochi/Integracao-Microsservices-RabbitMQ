from django.contrib import admin
from django.urls import path, include
from users.views import UserViewSet

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r"usuarios", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('admin/', admin.site.urls),
]

