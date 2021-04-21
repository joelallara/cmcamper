from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "core/index.html"

class ProductPageView(TemplateView):
    template_name = "core/products.html"

class OffRoadPageView(TemplateView):
    template_name = "core/off-road.html"

class MotorHomePageView(TemplateView):
    template_name = "core/motorhome.html"
