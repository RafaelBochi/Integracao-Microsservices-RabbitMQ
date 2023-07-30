from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from todo_list.views import ListViewSet
from usuario.router import router as usuario_router

router = DefaultRouter()
router.register(r"lists", ListViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/", include(usuario_router.urls)),
]
