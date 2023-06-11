from django.db import models

# Create your models here.

class Area(models.Model):
    area_id = models.AutoField(primary_key=True)
    estado_area = models.BooleanField()
    area_descripcion = models.CharField(max_length=20)
    fecha_insercion = models.DateTimeField(null=True)
    usuario_insercion = models.CharField(max_length=20, null=True)
    fecha_modificacion = models.DateTimeField(null=True)
    usuario_modificacion = models.CharField(max_length=16,blank=True, null=True)
    
    def __str__(self):
        return self. area_descripcion
    
    class Meta:
        db_table = "area"
        
        
class Persona(models.Model):
    persona_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nro_celular = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    fecha_insercion= models.DateTimeField(null=True)
    usuario_modificacion = models.CharField(max_length=20,blank=True,null=True)
    fecha_modificacion = models.DateTimeField(null=True)
    usuario_insercion = models.CharField(max_length=20,blank=True,null=True)
    estado_persona = models.BooleanField()
    
    def __str__(self):
        return self. nombre
    def __str__(self):
        return self. apellido
    def __str__(self):
        return self. nro_celular
    def __str__(self):
        return self. direccion
    
    class Meta:
        db_table = "persona"

class Condición(models.Model):
    condicion_id = models.AutoField(primary_key=True)
    condicion_descripcion = models.CharField(max_length=25)
    normal = models.BooleanField()
    discapacidad = models.BooleanField()
    embarazada = models.BooleanField()
    tercera_edad = models.BooleanField()
    fecha_insercion= models.DateTimeField(null=True)
    usuario_modificacion = models.CharField(max_length=20,blank=True,null=True)
    fecha_modificacion = models.DateTimeField(null=True)
    usuario_insercion = models.CharField(max_length=20,blank=True,null=True)
    estado_condicion  = models.BooleanField()
    
    def __str__(self):
        return self . condicion_descripcion
    
    
    class Meta:
        db_table = "condicion"
        
class Permisos(models.Model):
    permiso_id = models.AutoField(primary_key=True)
    permiso_descripcion = models.CharField(max_length=100)
    usuario_insercion = models.CharField(max_length=20,blank=True,null=True)
    fecha_insercion= models.DateTimeField(null=True)
    usuario_modificacion = models.CharField(max_length=20,blank=True,null=True)
    fecha_modificacion = models.DateTimeField(null=True)
    estado_permisos  = models.BooleanField()
    
    def __str__(self):
        return self.permiso_descripcion
    
    class Meta:
        db_table = "permisos"
    

class Prioridad(models.Model):
    prioridad_id = models.AutoField(primary_key=True)
    prioridad_descripcion = models.CharField(max_length=100)
    nivel = models.CharField(max_length=20)
    usuario_insercion = models.CharField(max_length=20,blank=True,null=True)
    fecha_insercion= models.DateTimeField(null=True)
    usuario_modificacion = models.CharField(max_length=20,blank=True,null=True)
    fecha_modificacion = models.DateTimeField(null=True)
    estado_prioridad = models.BooleanField()
    
    def __str__(self):
        return self.prioridad_descripcion
    def __str__(self):
        return self.nivel
    
    class Meta:
        db_table = "prioridad"