from django.urls import path
from .views import PrivacyView, TermsView, ContactView, AboutView, ContactSuccessView

urlpatterns = [
    path('privacidad/', PrivacyView.as_view(), name="privacy"),
	path('terminos/', TermsView.as_view(), name="terms"),
	path('nosotros/', AboutView.as_view(), name="about"),
	path('contacto/', ContactView.as_view(), name="contact"),
	path('contacto_exitoso/', ContactSuccessView.as_view(), name="contact_success"),
]