from django import forms
from .models import Contact
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget,PhoneNumberInternationalFallbackWidget
from ckeditor.widgets import CKEditorWidget
from .models import Contact

class ContactForm(forms.ModelForm):
    
    REASON_CHOICES = (
        ('default','Seleccione razón de contacto'),
        ('sub','Problema con pago o suscripción'),
        ('cuenta','Problemas con mi cuenta / acceso a mi cuenta'),
        ('trabajo','Bolsa de trabajo'),
        ('otro','Otra razón (mencionar en descripción)')
    )

    phone = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(initial='MX'),
        required=True)

    contact_reason = forms.ChoiceField(
        required=True, 
        choices=REASON_CHOICES
        )

    description = forms.CharField(
        required=False,
        widget=CKEditorWidget(),
    )

    class Meta:
        model = Contact
        fields = ('name',
                  'email',
                  'phone',
                  'contact_reason',
                  'description'
        )