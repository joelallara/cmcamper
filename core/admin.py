from django.contrib import admin
from .models import Portada, ListadoEquipamiento, ListadoAccesorios, Contacto, GaleriaProductos, GaleriaPopup, GaleriaMotorHome, GaleriaOffRoad, SobreNosotros


class PortadaAdmin(admin.ModelAdmin):
    list_display = ('titulo','imagen','orden',)

class SobreNosotrosAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)

class ListadoEquipamientoAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)

class ListadoAccesoriosAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)

class ContactoAdmin(admin.ModelAdmin):
    list_display = ('direccion','localidad','telefono','email','numero_wspp','link_facebook')

class GaleriasAdmin(admin.ModelAdmin):
    list_display = ('imagen','orden')

class GaleriaProductosAdmin(GaleriasAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(GaleriaProductosAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['orden'].initial = (GaleriaProductos.objects.count()+1)
        return form

class GaleriaPopupAdmin(GaleriasAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(GaleriaPopupAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['orden'].initial = (GaleriaPopup.objects.count()+1)
        return form

class GaleriaMotorHomeAdmin(GaleriasAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(GaleriaMotorHomeAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['orden'].initial = (GaleriaMotorHome.objects.count()+1)
        return form

class GaleriaOffRoadAdmin(GaleriasAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(GaleriaOffRoadAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['orden'].initial = (GaleriaOffRoad.objects.count()+1)
        return form

admin.site.register(Portada,PortadaAdmin)
admin.site.register(SobreNosotros,SobreNosotrosAdmin)
# admin.site.register(ListadoEquipamiento,ListadoEquipamientoAdmin)
# admin.site.register(ListadoAccesorios,ListadoAccesoriosAdmin)
admin.site.register(Contacto,ContactoAdmin)
# admin.site.register(GaleriaProductos,GaleriaProductosAdmin)
admin.site.register(GaleriaPopup,GaleriaPopupAdmin)
admin.site.register(GaleriaMotorHome,GaleriaMotorHomeAdmin)
admin.site.register(GaleriaOffRoad,GaleriaOffRoadAdmin)

