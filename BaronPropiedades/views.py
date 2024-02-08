from django.shortcuts import render, redirect
from django.db.models import OuterRef
from .models import Client, Property, PropertyImage, InterestedPropertyClient
from .forms import ClientForm
from django.views.generic import TemplateView, ListView
from django.contrib import messages
from django.core.paginator import Paginator




"""
==============
    INDEX
==============
-GET renders index.html template.
-POST handles new_client form - returns success/error messages.

"""

class index(TemplateView):
    template_path = "index.html"
    client_form = ClientForm
    context_variables = {
        "client_form" : ClientForm
    }

    def get(self, request):
        return render(request, self.template_path, self.context_variables)
    
    def post(self, request):
        if request.method == "POST":
            form = ClientForm(request.POST)
        
        if form.is_valid():
            # Process the valid form data and save it to the database
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']

            new_client = Client(name=name, email=email, phone=phone)
            new_client.save()
            
            messages.success(request, "¡Gracias por registrarte! Te contactaremos a la brevedad")
            return redirect('index')
        
        else:
            messages.error(request, "Usted ya está registrado(a), ¡Lo(a) contactaremos a la brevedad! ")
            print(form.errors)
            return redirect('index')
        

"""
===========================
    PROPERTY CATALOGUE
===========================
-GET renders catalogue.html template. Every property with its thumbnail.

"""

class catalogue(ListView):
    model = Property
    template_path = "catalogue.html"
    client_form = ClientForm
    context_variables = {
        "client_form" : ClientForm,
    }

    def get(self, request):
        
        # Properties objects
        properties = Property.objects.all()

        # Add property thumbnail path to property objects
        for p in properties:
            p.thumbnail_path = PropertyImage.objects.filter(property_id=p.id, is_thumbnail=True).first

        # Paginator
        paginator_instance = Paginator(properties, 10)
        page_number = request.GET.get("page")
        properties_per_page = paginator_instance.get_page(page_number)

        # Add properties to pagecontext
        self.context_variables["properties_per_page"] = properties_per_page

        # Renders page
        return render(request, self.template_path, self.context_variables)

    def post(self, request):
        pass



"""
===========================
    PROPERTY VIEWER
===========================
-GET; Shows property info, with images, details and form button.
-POST; Handles the form info submission.

"""

class property_info(ListView):
    model = {Property, PropertyImage}
    template_path = "property-info.html"
    client_form = ClientForm
    context_variables = {
        "client_form" : ClientForm,
    }

    def get(self, request, id):
        # Get instances
        property = Property.objects.get(id=id)
        images = PropertyImage.objects.filter(property_id=id)

        # Add data to page context
        self.context_variables["property"] = property
        self.context_variables["images_path"] = images

        return render(request, self.template_path, self.context_variables)
        
    def post(self, request, id):
        # Client info + Property they're interested in...
        if request.method == "POST":
            
            # Client info
            name = request.POST.get("name")
            mail = request.POST.get("email")
            phone = request.POST.get("phone")
            
            # Interested property instance
            property_id = id
            property= Property.objects.get(id=property_id)

            # Create new client if not exists / Get instance
            if not (Client.objects.filter(email=mail)):
                #new_client = Client(name=name, email=mail, phone=phone)
                #new_client.save()
                Client.objects.create(name=name, email=mail, phone=phone)
                client = Client.objects.get(email = mail, phone = phone)

            # Get cient instance if exists
            else:
                client = Client.objects.get(email = mail, phone = phone)

            # Save new Interested Property Client
            new_interested_client = InterestedPropertyClient(client=client, property=property)
            new_interested_client.save()
            #InterestedPropertyClient.objects.create(client=client, property=property)

            # Success message & redirect
            messages.success(request, "Hemos recibido tu solicitud ¡Te contactaremos a la brevedad!")
            return redirect(request.path)
        

"""
==================
ERROR 404 HANDLER
==================
"""
def handler404(request, exception):
    template_name = '404.html'
    context = {
        'exception': exception
    }
    return render(request, template_name, context)


"""
==================
ERROR 500 HANDLER
==================
"""
def handler500(request, *args, **argv):
    template_name = '500.html'
    return render(request, template_name)


"""
================
    LEGAL
================
"""

def legal_advise(request):
    template_name = 'legal-advise.html'
    return render(request, template_name)

def privacy_policy(request):
    template_name = 'privacy-policies.html'
    return render(request, template_name)
