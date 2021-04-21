from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "core/index.html"

class ProductPageView(TemplateView):
    template_name = "core/products.html"
