from django.contrib import admin
from .models import Region, Comuna, ServiceType, PropertyType, Property, PropertyImage, InterestedPropertyClient, Client
from .forms import ImageForm

# Model admin
class AdminRegion(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    ordering = ('-created_at',)

class AdminComuna(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    ordering = ('-created_at',)

class AdminServiceType(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    ordering = ('-created_at',)

class AdminPropertyType(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    ordering = ('-created_at',)

class AdminInlineImages(admin.TabularInline):
    readonly_fields=['property']
    model = PropertyImage
    form = ImageForm
    
class AdminProperty(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')
    list_display = ('property_type','service_type','comuna','price','is_UF','is_available')
    search_fields = ('comuna',)
    list_filter = ('property_type','service_type','comuna','rooms','baths','is_UF')
    ordering = ('-created_at',)
    inlines = [AdminInlineImages,]

class AdminInterestedPropertyClient(admin.ModelAdmin):
    readonly_fields = ('client','property','created_at',)
    search_fields = ('client',)
    ordering = ('-created_at',)

class AdminClient(admin.ModelAdmin):
    readonly_fields = ('name','email','phone')
    list_display = ('name','email','phone')
    search_fields = ('name',)
    ordering = ('-created_at',)


# Register your models here.
admin.site.register(Region, AdminRegion)
admin.site.register(Comuna, AdminComuna)
admin.site.register(ServiceType, AdminServiceType)
admin.site.register(PropertyType, AdminPropertyType)
admin.site.register(Property, AdminProperty)
admin.site.register(Client, AdminClient)
admin.site.register(InterestedPropertyClient, AdminInterestedPropertyClient)


# Admin site config
title = 'BARON PROPIEDADES CL'
subtitle = 'Panel de administración'
admin.site.index_title = title
admin.site.site_header = subtitle
admin.site.site_title = subtitle

# Customize Django Admin panel
# Globally disable delete selected
admin.site.disable_action("delete_selected")