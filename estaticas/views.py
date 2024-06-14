from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Contact
from .forms import ContactForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


# Create your views here.
class PrivacyView(TemplateView):
    template_name = "estaticas/privacidad.html"

class AboutView(TemplateView):
    template_name = "estaticas/nosotros.html"

class TermsView(TemplateView):
    template_name = "estaticas/terminos.html"

class ContactSuccessView(TemplateView):
    template_name = "estaticas/contact_success.html"

class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('contact_success')
