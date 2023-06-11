from django.contrib import admin
from . import models
# Register your models here.

class AreaAdmin(admin.ModelAdmin):
    list_display =["area_descripcion","estado_area","fecha_insercion"]
    list_filter =["fecha_insercion"]
    list_editable =["estado_area","fecha_insercion"]
    search_fields =["area_descripcion"]
    
admin.site.register(models.Area, AreaAdmin)

class PersonaAdmin(admin.ModelAdmin):
    list_display =["nombre","apellido","nro_celular"]
    list_filter =["nombre"]
    list_editable =[]
    search_fields =["nombre", "apellido"]
    
admin.site.register(models.Persona, PersonaAdmin)

class CondiciónAdmin(admin.ModelAdmin):
    list_display =["condicion_descripcion"]
    list_filter =[]
    list_editable =[]
    search_fields =["condicion_descripcion"]
    
admin.site.register(models.Condición, CondiciónAdmin    )

class PermisosAdmin(admin.ModelAdmin):
    list_display =["permiso_descripcion","usuario_insercion"]
    list_filter =[]
    list_editable =["usuario_insercion"]
    search_fields =[]
    
admin.site.register(models.Permisos, PermisosAdmin)

class PrioridadAdmin(admin.ModelAdmin):
    list_display =["prioridad_descripcion","nivel","usuario_insercion"]
    list_filter =["estado_prioridad"]
    list_editable =["usuario_insercion"]
    search_fields =[]
    
admin.site.register(models.Prioridad, PrioridadAdmin)