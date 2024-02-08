"""
URL configuration for BaronPropieadesWebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from BaronPropiedades import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('222/', admin.site.urls),
    path('', views.index.as_view(), name="index"),
    path('inicio/', views.index.as_view(), name="index"),
    path('catalogo-propiedades/', views.catalogue.as_view(), name="catalogue"),
    path('propiedad/<int:id>/', views.property_info.as_view(), name="property"),
    path('aviso-legal/', views.legal_advise, name="legal"),
    path('pollitica-de-privacidad/', views.privacy_policy, name="privacy"),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'BaronPropiedades.views.handler404'
handler500 = 'BaronPropiedades.views.handler500'

#path('500', views.error_500, name="500")
#path('404', views.error_404, name="404"),
