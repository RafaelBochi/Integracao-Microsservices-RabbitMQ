from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from todo_list.views import ListViewSet

router = DefaultRouter()
router.register(r"lists", ListViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]