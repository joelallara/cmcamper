from django.urls import path
from .views import HomePageView, ProductPageView

urlpatterns = [
    path('', HomePageView.as_view(), name="inicio"),
    path('productos/', ProductPageView.as_view(), name="productos")
]