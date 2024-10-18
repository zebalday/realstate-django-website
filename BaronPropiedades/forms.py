from django import forms
from django.forms import ModelForm
from .models import Client, Property, PropertyImage
from phonenumber_field.modelfields import PhoneNumberField


"""
===========
CLIENT FORM
===========
-name
-email
-phone

"""
class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = [
            "name",
            "email",
            "phone"
        ]
        widgets = {
            "name" : forms.TextInput(attrs={'class':'form-input',
                                            'placeholder':'Nombre',
                                            'title':'Ingrese su nombre'
                                            }),
            "email" : forms.EmailInput(attrs={'class':'form-input',
                                            'placeholder':'Email',
                                            'title':'Correo electrónico'
                                            }),
            "phone" : forms.TextInput(attrs={'class':'form-input',
                                            'placeholder':'Teléfono (+569...)',
                                            'type': 'tel',
                                            'pattern': '^\+569\d{8}$',
                                            'maxlenght':'12',
                                            'title':'Número telefónico (+569XXXXXXXX)'
                                            })
        }
        labels = {
            "name" : False,
            "email" : False,
            "phone" : False
        }

"""
===========
IMAGE FORM
===========
- property (fk)
- image (select multiple files)

"""
class ImageForm(forms.ModelForm):
    class Meta:
        model= PropertyImage
        fields = [
            "property",
            "image",
            "is_thumbnail"
        ]
        widgets = {
            "image": forms.ClearableFileInput(attrs={"multiple":False})
        }
        labels = {
            "image":"Imágenes"
        }


"""
======================
INTERESTED CLIENT FORM
======================
-name
-email
-phone

"""
class InterestedPropertyClientForm(forms.ModelForm):
    class Meta:
        fields=[
            'client',
            'property',
        ]
