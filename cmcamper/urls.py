from django.contrib import admin
from django.urls import path, include

from django.config import settings
from django.config.urls.static import static

urlpatterns = [
    path('', include('core.urls')),

    path('admin/', admin.site.urls),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
