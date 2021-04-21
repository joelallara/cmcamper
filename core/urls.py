from django.urls import path
from .views import HomePageView, ProductPageView, OffRoadPageView, MotorHomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name="inicio"),
    path('pop-up/', ProductPageView.as_view(), name="productos"),
    path('off-road/', OffRoadPageView.as_view(), name="offroad"),
    path('motorhome/', MotorHomePageView.as_view(), name="motorhome")
]