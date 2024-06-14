from django import forms
from .models import PostPerson, PostRoom
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget,PhoneNumberInternationalFallbackWidget
from ckeditor.widgets import CKEditorWidget
from django.utils.safestring import mark_safe


class PostPersonForm(forms.ModelForm):
    
    GENDER_CHOICES = (
        ('hombre','Hombre'),
        ('mujer','Mujer'),
        ('otro','Otro'),
        ('mixto','Mixto')
    )
    PLACE_CHOICES = (
        ('casa','Casa'),
        ('departamento','Departamento'),
        ('otro','Otros')
    )
    AMENITIES_CHOICES = (
        ('servicios','Servicios incluidos'),
        ('wifi','Wi-Fi'),
        ('estacionamiento','Estacionamiento'),
        ('limpieza','Limpieza incluida'),
        ('gym','Gym'),
        ('elevador','Elevador'),
        ('bano','Baño propio'),
        ('facturacion','Facturacion'),
        ('cocina','Acceso a cocina'),
        ('comida','Preparación de comidas'),
        ('mascotas','Acepten mascotas'),
        ('visitas','Acepten visitas'),
        ('infantes','Acepten infantes'),
        ('lavadora','Lavadora'),
        ('secadora','Secadora'),
        ('directo','Trato directo'),
    )

    image = forms.ImageField(required=False, 
                                widget = forms.FileInput(
        attrs={'class':'form-control', 
               'onchange' : 'preview(event)' } 
         ))

    
    phone = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(initial='MX'),
        required=True)
    gender = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect, 
        choices=GENDER_CHOICES
        )
    name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'onkeyup':"textCounter(this,'counter1',120);",
                                      'class':'form-control'
                                      })
        )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'onkeyup':"textCounter(this,'counter2',800);",
                                      'class':'form-control'
                                      })
        )
    amenities = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple, 
        choices=AMENITIES_CHOICES
        )
    class Meta:
        model = PostPerson
        fields = ('image',
                  'name',
                  'description',
                  'gender',
                #   'colonia',
                #   'municipio',
                #   'estado',
                  'longitud',
                  'latitud',
                  'smokes',
                  'amount',
                  'amenities',
                  'phone',
                  'whatsapp',
                  'price')
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     self.fields['estado'].required = True
    #     self.fields['municipio'].required = True
    #     self.fields['colonia'].required = True

    #     self.fields['municipio'].queryset = Municipio.objects.none()
    #     self.fields['colonia'].queryset = Colonia.objects.none()

    #     if 'estado' in self.data:
    #         try:
    #             estado_id = int(self.data.get('estado'))
    #             self.fields['municipio'].queryset = Municipio.objects.filter(estado_id=estado_id).order_by('municipio')
    #         except (ValueError, TypeError):
    #             pass  # invalid input from the client; ignore and fallback to empty City queryset
    #     elif self.instance.pk:
    #         self.fields['municipio'].queryset = self.instance.estado.municipio_set.order_by('municipio')

    #     if 'municipio' in self.data:
    #         try:
    #             municipio_id = int(self.data.get('municipio'))
    #             self.fields['colonia'].queryset = Colonia.objects.filter(municipio_id=municipio_id).order_by('colonia')
    #         except (ValueError, TypeError):
    #             pass  # invalid input from the client; ignore and fallback to empty City queryset
    #     elif self.instance.pk:
    #         self.fields['colonia'].queryset = self.instance.municipio.colonia_set.order_by('colonia')



class PostRoomForm(forms.ModelForm):
    
    GENDER_ROOM_CHOICES = (
        ('hombre','Hombres'),
        ('mujer','Mujeres'),
        ('otro','Cualquier género')
    )

    SMOKERS_CHOICES = (
        ('si','Acepto fumadores'),
        ('no','No acepto fumadores'),
        ('afuera','Sólo afuera')
    )

    PLACE_CHOICES = (
        ('casa','Casa'),
        ('departamento','Departamento'),
        ('otro','Otros')
    )

    AMENITIES_CHOICES = (
        ('servicios','Servicios incluidos'),
        ('wifi','Wi-Fi'),
        ('estacionamiento','Estacionamiento'),
        ('limpieza','Limpieza incluida'),
        ('gym','Gym'),
        ('elevador','Elevador'),
        ('bano','Baño propio'),
        ('facturacion','Facturacion'),
        ('cocina','Acceso a cocina'),
        ('comida','Preparación de comidas'),
        ('mascotas','Acepten mascotas'),
        ('visitas','Acepten visitas'),
        ('infantes','Acepten infantes'),
        ('lavadora','Lavadora'),
        ('secadora','Secadora'),
        ('directo','Trato directo')
    )

    image1 = forms.ImageField(required=False, 
                                widget = forms.FileInput(
        attrs={'class':'form-control', 
               'onchange' : 'preview_1(event)' } 
         ))

    image2 = forms.ImageField(required=False, 
                                widget = forms.FileInput(
        attrs={'class':'form-control', 
               'onchange' : 'preview_2()' } 
         ))

    image3 = forms.ImageField(required=False, 
                                widget = forms.FileInput(
        attrs={'class':'form-control', 
               'onchange' : 'preview_3()' } 
         ))

    image4 = forms.ImageField(required=False, 
                                widget = forms.FileInput(
        attrs={'class':'form-control', 
               'onchange' : 'preview_4()' } 
         ))

    image5 = forms.ImageField(required=False, 
                                widget = forms.FileInput(
        attrs={'class':'form-control', 
               'onchange' : 'preview_5()' } 
         ))

    image6 = forms.ImageField(required=False,
                                widget = forms.FileInput(
        attrs={'class':'form-control', 
               'onchange' : 'preview_6()' } 
         ))
             
    phone = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(initial='MX'),
        required=True)

    gender = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect, 
        choices=GENDER_ROOM_CHOICES
        )
    
    place = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect, 
        choices=PLACE_CHOICES
        )

    smokers = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect, 
        choices=SMOKERS_CHOICES
        )
    
    
    title = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'onkeyup':"textCounter(this,'counter1',120);",
                                      'class':'form-control'
                                      })
    )

    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'onkeyup':"textCounter(this,'counter2',800);",
                                      'class':'form-control'
                                      })
    )

    min_amount = forms.IntegerField(required=False,
                                    min_value=1)

    max_amount = forms.IntegerField(required=False,
                                    min_value=1)

    amenities = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple, 
        choices=AMENITIES_CHOICES
        )

    class Meta:
        model = PostRoom
        fields = ('title',
                #   'colonia',
                #   'municipio',
                #   'estado',
                  'longitud',
                  'latitud',
                  'image1',
                  'image2',
                  'image3',
                  'image4',
                  'image5',
                  'image6',
                  'description',
                  'gender',
                  'place',
                  'smokers',
                  'several',
                  'min_amount',
                  'max_amount',
                  'price_extra',
                  'amenities',
                  'phone',
                  'whatsapp',
                  'price',
                  'deposit_check',
                  'deposit_amount')

