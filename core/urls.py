from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePageView, PopUpPageView, OffRoadPageView, MotorHomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name="inicio"),
    path('pop-up/', PopUpPageView.as_view(), name="popup"),
    path('camiones/', OffRoadPageView.as_view(), name="camiones"),
    path('motorhome/', MotorHomePageView.as_view(), name="motorhome")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)