from django.contrib import admin
from django.urls import path

from core.views import Homepage

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", Homepage.as_view(), name="homepage"),
]
