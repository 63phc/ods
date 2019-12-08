from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('src.apps.account.urls')),
    path('panel/', include('src.apps.panel.urls')),
]
