from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

# Create your models here.

"""
==================
CLIENT CLASS MODEL
==================
-name
-email
-phone
-created_at

"""

class Client(models.Model):
    name = models.TextField(
        max_length = 150,
        verbose_name = "Nombre",
        blank = False,
        null = False,
        editable = True
    )
    email = models.EmailField(
        max_length = 250,
        verbose_name = "Correo",
        blank = False,
        null = False,
        unique = True,
        editable = True
    )
    phone = PhoneNumberField(
        region = "CL",
        verbose_name = "Teléfono",
        blank = False,
        null = False,
        unique = False,
        editable = True
    )
    created_at = models.DateTimeField(
        verbose_name = "Creado el",
        auto_now_add = True
    )

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["-created_at"]
    
    def __str__(self):
        return (f"{self.name}")
    

# Send email with new client info
@receiver(post_save, sender=Client)
def send_new_client_info(sender, instance, created,  **kwargs):
    if created:
        message = f"""Nueva persona registrada.\n\nNombre: {instance.name}\nCorreo: {instance.email}\nTeléfono: {instance.phone}"""

        send_mail(
            subject="Nueva persona registrada!",
            message=message,
            from_email= settings.EMAIL_HOST_USER,
            recipient_list=["baron@baronpropiedades.cl","baronpropiedades@gmail.com"],
            fail_silently=False
        )




"""
==================
REGION CLASS MODEL
==================
-name
-created_at
-updated_at

"""
class Region(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Región",
        blank=False,
        null=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Creada el'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Actualizada el'
    )

    class Meta:
        verbose_name = 'Región'
        verbose_name_plural = 'Regiones'
        ordering = ["-created_at"]

    def __str__(self):
        return (self.name)
    


"""
==================
COMUNA CLASS MODEL
==================
-name
-created_at
-updated_at

"""
class Comuna(models.Model):
    region = models.ForeignKey(
        Region,
        on_delete = models.CASCADE,
        editable=True,
        blank = False,
        null = False
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Comuna",
        editable = True,
        blank=False,
        null=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Creada el'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Actualizada el'
    )

    class Meta:
        verbose_name = 'Comuna'
        verbose_name_plural = 'Comunas'
        ordering = ["-created_at"]

    def __str__(self):
        return (self.name)
    


"""
==================
SERVICE TYPE CLASS MODEL
==================
-name
-created_at
-updated_at

"""
class ServiceType(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Tipo de servicio",
        editable=True,
        blank=False,
        null=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Creado el'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Actualizado el'
    )

    class Meta:
        verbose_name = 'Tipo de servicio'
        verbose_name_plural = 'Tipos de servicios'
        ordering = ["-created_at"]
    
    def __str__(self):
        return (self.name)

"""
==================
PROPERTY TYPE CLASS MODEL
==================
-name
-created_at
-updated_at

"""
class PropertyType(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Tipo de propiedad",
        editable=True,
        blank=False,
        null=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Creado el'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Actualizado el'
    )

    class Meta:
        verbose_name = 'Tipo de propiedad'
        verbose_name_plural = 'Tipos de propiedad'
        ordering = ["-created_at"]


    def __str__(self):
        return (self.name)
    


"""
==================
PROPERTY CLASS MODEL
==================
-tittle
-Property Type
-Service Type
-Comuna
-Address
-Price
-UF (BOOL)
-Squared Meters
-Rooms
-Baths
-Furniture (¿Está amoblado?)
-Internet (WI-FI)
-TV
-Laundry (Lavadora)
-Parking (Estacionamiento)
-Store (Bodega)
-Balcony (Balcón)
-Elevator (Ascensor)
-Pool (Tiene piscina)
-created_at
-updated_at

"""

class Property(models.Model):

    """ BASIC INFORMATION """
    title = models.CharField(
        max_length=150,
        verbose_name="Título",
        editable=True,
        blank=False,
        null=False
    )
    description = RichTextField(
        editable = True,
        null = True,
        blank = True,
        verbose_name = "Breve descripción"
    )
    property_type = models.ForeignKey(
        PropertyType,
        editable=True,
        verbose_name="Tipo de propiedad",
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    service_type = models.ForeignKey(
        ServiceType,
        editable=True,
        verbose_name="Tipo de servicio",
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    comuna = models.ForeignKey(
        Comuna,
        editable=True,
        verbose_name = "Comuna",
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    address = models.CharField(
        max_length = 150,
        editable=True,
        verbose_name = "Dirección",
        blank=False,
        null=False
    )
    price = models.IntegerField(
        editable=True,
        validators=[MinValueValidator(0)],
        verbose_name = "Precio",
        blank=False,
        null=False
    )
    is_UF = models.BooleanField(
        default=False,
        editable=True,
        verbose_name="¿Precio en UF?",
    )
    squared_meters = models.FloatField(
        editable = True,
        validators=[MinValueValidator(0.0)],
        verbose_name="Metros cuadrados",
        blank=False,
        null=False
    )
    rooms = models.IntegerField(
        editable = True,
        validators=[MinValueValidator(0)],
        verbose_name="Número de dormitorios",
        blank=False,
        null=False
    )
    baths = models.IntegerField(
        editable = True,
        validators=[MinValueValidator(0)],
        verbose_name="Número de baños",
        blank=False,
        null=False
    )

    """ HOUSE/APARTMENT CARACTERISTICS """
    has_furnitures = models.BooleanField(
        default=False,
        editable=True,
        verbose_name="¿Está amoblado?",
    )
    has_internet = models.BooleanField(
        default=False,
        editable=True,
        verbose_name="¿Tiene Wi-Fi?",
    )
    has_tv = models.BooleanField(
        default=False,
        editable=True,
        verbose_name="¿Tiene Televisión?",
    )
    has_laundry = models.BooleanField(
        default=False,
        editable=True,
        verbose_name="¿Tiene lavadora?",
    )
    has_parking = models.BooleanField(
        default=False,
        editable=True,
        verbose_name="¿Tiene estacionamiento?",
    )
    has_storage = models.BooleanField(
        default=False,
        editable=True,
        verbose_name="¿Tiene bodega?",
    )
    has_balcony = models.BooleanField(
        default=False,
        editable=True,
        verbose_name="¿Tiene balcón?",
    )
    has_elevator = models.BooleanField(
        default=False,
        editable=True,
        verbose_name="¿Tiene ascensor?",
    )
    has_pool = models.BooleanField(
        default=False,
        editable=True,
        verbose_name="¿Tiene piscina?",
    )

    """ TERRAIN CHARACTERISTICS """
    has_energy_disposal = models.BooleanField(
        default=False,
        editable=True,
        verbose_name="¿Tiene disponibilidad de luz?",
    )
    has_water_disposal = models.BooleanField(
        default=False,
        editable=True,
        verbose_name="¿Tiene disponibilidad de agua?",
    )

    """ TIMESTAMPS """
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Creada el'
    )
    updated_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Actualizada el'
    )

    """ AVAILABLE """
    is_available = models.BooleanField(
        default = True,
        editable = True,
        verbose_name = "¿Disponible?",
    )


    """ META """
    class Meta:
        verbose_name = "Propiedad"
        verbose_name_plural = "Propiedades"
        ordering = ['-created_at']
    
    def __str__(self):
        return (f"({self.property_type}) - {self.title}")
        

# Creates different folder for each created property
def get_image_upload_path(instance, filename):
    # Define the upload path based on the property_id
    upload_path = f"property{instance.property.id}/{filename}"
    return upload_path

# Validates image max size (3MB)
def validate_image_size(value):
    if value.size > 1024 * 1024 * 3:
        raise ValidationError("La imagen es muy grande (máx 3 MB). Comprímala.")
    

"""
==================
IMAGE CLASS MODEL
==================
-property
-image
-is_thumbnail

"""

class PropertyImage(models.Model):
    property = models.ForeignKey(
        Property,
        verbose_name = "Fotos de propiedad",
        on_delete = models.CASCADE,
        blank=False,
        null=False
    )
    image = models.ImageField(
        upload_to= get_image_upload_path,
        validators=[validate_image_size],
        null = True,
        blank= True
    )
    is_thumbnail = models.BooleanField(
        verbose_name = "¿Mostrar imagen como miniatura?",
        editable = True,
        default = False,
        null = True,
        blank= True
    )

    class Meta:
        verbose_name = "Imagen"
        verbose_name_plural = "Imágenes"


"""
=============================
INTERESTED CLIENT CLASS MODEL
=============================
-client
-property
-created_at

"""

class InterestedPropertyClient(models.Model):
    client = models.ForeignKey(
        Client,
        verbose_name = "Cliente interesado",
        on_delete = models.PROTECT,
        editable = False,
        null = False,
        blank = False
    )
    property = models.ForeignKey(
        Property,
        verbose_name = "Propiedad de interés",
        on_delete = models.PROTECT,
        editable=False,
        null = False,
        blank = False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Creada el'
    )

    class Meta:
        verbose_name = "Cliente interesado"
        verbose_name_plural = "Clientes interesados"

    def __str__(self):
        return (f"{self.client.name} está interesado(a) en {self.property.title}")
    

# Send email with new client info
@receiver(post_save, sender=InterestedPropertyClient)
def send_new_interested_client_info(sender, instance, created,  **kwargs):
    if created:
        message = f"""Nueva persona interesada!\n\nLa Propiedad [ {instance.property} ] tiene una persona interesada.\n\nNombre: {instance.client.name}\nCorreo: {instance.client.email}\nTeléfono: {instance.client.phone}"""

        send_mail(
            subject="Nueva persona interesada!",
            message=message,
            from_email= settings.EMAIL_HOST_USER,
            recipient_list=["baron@baronpropiedades.cl","baronpropiedades@gmail.com"],
            #recipient_list=["sebaalday28@gmail.com"],
            fail_silently=False
        )