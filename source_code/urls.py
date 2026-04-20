"""
Endpoint root configuration
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('leads/', include('leads.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('', include('dashboard.urls')),
]
