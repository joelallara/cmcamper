from django.urls import path
from .views import HomePageView, PopUpPageView, OffRoadPageView, MotorHomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name="inicio"),
    path('pop-up/', PopUpPageView.as_view(), name="popup"),
    path('off-road/', OffRoadPageView.as_view(), name="offroad"),
    path('motorhome/', MotorHomePageView.as_view(), name="motorhome")
]