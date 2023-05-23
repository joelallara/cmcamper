from django.shortcuts import render
from django.views.generic.base import TemplateView
from core.models import Portada, ListadoEquipamiento, ListadoAccesorios, Contacto, GaleriaProductos, GaleriaPopup, GaleriaMotorHome, GaleriaOffRoad, SobreNosotros


class HomePageView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['equipamientos'] = ListadoEquipamiento.objects.all()
        context['accesorios'] = ListadoAccesorios.objects.all()
        context['contactos'] = Contacto.objects.all()
        context['productos'] = GaleriaProductos.objects.all()
        context['nosotros'] = SobreNosotros.objects.all()
        context['portadas'] = Portada.objects.all()
        return context

class PopUpPageView(HomePageView):
    template_name = "core/products.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fotos'] = GaleriaPopup.objects.all()
        return context

class OffRoadPageView(HomePageView):
    template_name = "core/off-road.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fotos'] = GaleriaOffRoad.objects.all()
        return context

class MotorHomePageView(HomePageView):
    template_name = "core/motorhome.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fotos'] = GaleriaMotorHome.objects.all()
        return context