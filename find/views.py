from django.db.models.query import QuerySet
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import TemplateView
from posts.models import PostRoom, PostPerson
from registration.models import Profile

def check_in_request_get(request,parameter):
    if request.method == 'GET' and parameter in request.GET:
        variable = request.GET[parameter]
        if variable == '':
            variable = 0
    else:
        variable = 0
    return variable


class FindGeneralView(TemplateView):
    template_name = "find/find_general.html"



#VISTA CON FORMS.PY
def room_results(request):

    if request.method == 'GET':
        norte = float(check_in_request_get(request,'norte'))
        sur = float(check_in_request_get(request,'sur'))
        este = float(check_in_request_get(request,'este'))
        oeste = float(check_in_request_get(request,'oeste'))
        lat_centro = float(check_in_request_get(request,'lat_centro'))
        lon_centro = float(check_in_request_get(request,'lon_centro'))
        nivel_zoom = float(check_in_request_get(request,'nivel_zoom'))
        minP = int(check_in_request_get(request,'minPrice'))  
        maxP = int(check_in_request_get(request, 'maxPrice'))
        personAmt = int(check_in_request_get(request, 'personAmt'))
        gender = check_in_request_get(request, 'gender')
        smoker = check_in_request_get(request,'smoker')
        servicios = check_in_request_get(request,'servicios')
        wifi = check_in_request_get(request, 'wifi')
        estacionamiento = check_in_request_get(request,'estacionamiento')
        limpieza = check_in_request_get(request, 'limpieza')
        gym = check_in_request_get(request,'gym')
        elevador = check_in_request_get(request,'elevador')
        bano = check_in_request_get(request, 'bano')
        facturacion = check_in_request_get(request, 'facturacion')
        cocina = check_in_request_get(request, 'cocina')
        comida = check_in_request_get(request, 'comida')
        mascotas = check_in_request_get(request, 'mascotas')
        visitas = check_in_request_get(request, 'visitas')
        infantes = check_in_request_get(request, 'infantes')
        lavadora = check_in_request_get(request, 'lavadora')
        secadora = check_in_request_get(request, 'secadora')
        directo = check_in_request_get(request, 'directo')
        # estado = check_in_request_get(request, 'estado')
        # municipio = check_in_request_get(request, 'municipio')
        # colonia = check_in_request_get(request, 'colonia')
        orden = check_in_request_get(request, 'sort')
        # print ('ROOM FIND:','GET: estado',estado)


        
        queryset = PostRoom.objects.all()

        queryset = queryset.filter(
            paused__exact = False
        )

        # Por ubicación

        queryset = queryset.filter(
            latitud__lte = (norte+1),
            latitud__gte = (sur-1),
            longitud__lte = (este+1),
            longitud__gte = (oeste-1)

        )

                #ORDEN (SORT) DE RESULTADOS

        if orden == 'precioMenor':
            queryset = queryset.all().order_by('price')
        
        if orden == 'precioMayor':
            queryset = queryset.all().order_by('-price')
        

        if minP >= 1:
            queryset = queryset.filter(
                price__gte = minP
            )

        if maxP >= 1:
            queryset = queryset.filter(
                price__lte = maxP
            )
        
        if personAmt != 0:
            print ("0",queryset)
            queryset = queryset.filter(
                min_amount__lte = personAmt
            )
            print ("1",queryset)
            queryset = queryset.filter(
                max_amount__gte = personAmt
            )
            print ("2",queryset)

        if gender == 'mujer':
            queryset = queryset.filter(
                gender__exact='mujer'
            )
        elif gender == 'hombre':
            queryset = queryset.filter(
                gender__exact='hombre'
            )
        
        if smoker == 'on':
            queryset = queryset.filter(
                smokers__exact='no'
            )

        if servicios == 'on':
            queryset = queryset.filter(
                amenities__icontains='servicios'
            )

        if wifi == 'on':
            queryset = queryset.filter(
                amenities__icontains='wifi'
            )
        
        if estacionamiento == 'on':
            queryset = queryset.filter(
                amenities__icontains='estacionamiento'
            )
        
        if limpieza == 'on':
            queryset = queryset.filter(
                amenities__icontains='limpieza'
            )
        
        if gym == 'on':
            queryset = queryset.filter(
                amenities__icontains='gym'
            )
        
        if elevador == 'on':
            queryset = queryset.filter(
                amenities__icontains='elevador'
            )
        
        if bano == 'on':
            queryset = queryset.filter(
                amenities__icontains='bano'
            )
        

        if facturacion == 'on':
            queryset = queryset.filter(
                amenities__icontains='facturacion'
            )

        if cocina == 'on':
            queryset = queryset.filter(
                amenities__icontains='cocina'
            )

        if comida == 'on':
            queryset = queryset.filter(
                amenities__icontains='comida'
            )
        
        if mascotas == 'on':
            queryset = queryset.filter(
                amenities__icontains='mascotas'
            )
        
        if visitas == 'on':
            queryset = queryset.filter(
                amenities__icontains='visitas'
            )

        if infantes == 'on':
            queryset = queryset.filter(
                amenities__icontains='infantes'
            )

        if lavadora == 'on':
            queryset = queryset.filter(
                amenities__icontains='lavadora'
            )
        
        if secadora == 'on':
            queryset = queryset.filter(
                amenities__icontains='secadora'
            )

        if directo == 'on':
            queryset = queryset.filter(
                amenities__icontains='directo'
            )


    items = 50
    p = Paginator(queryset, items)
    page_num = request.GET.get('page',1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    
    lim = min(items,queryset.count())
    coords = []
    for i in range(0,lim):
        l_int = []
        lat = float(queryset.all()[i].latitud)
        lon = float(queryset.all()[i].longitud)
        l_int.append(lat)
        l_int.append(lon)
        coords.append(l_int)
    print(coords)
    

    context = {
            "rooms": page,
            #"form": form,
            "request":request
            }
        

    if request.user.is_authenticated:
        userid = request.user.id
        profile = get_object_or_404(Profile, user=userid)
        favorites = profile.room_favorites.all()
        if favorites:
            context["favorites"] = favorites


    return render(request, "find/find_room.html",context)

    

def person_results(request):



    if request.method == 'GET':
        norte = float(check_in_request_get(request,'norte'))
        sur = float(check_in_request_get(request,'sur'))
        este = float(check_in_request_get(request,'este'))
        oeste = float(check_in_request_get(request,'oeste'))
        lat_centro = float(check_in_request_get(request,'lat_centro'))
        lon_centro = float(check_in_request_get(request,'lon_centro'))
        nivel_zoom = float(check_in_request_get(request,'nivel_zoom'))
        minP = int(check_in_request_get(request,'minPrice'))  
        maxP = int(check_in_request_get(request, 'maxPrice'))
        personAmt = int(check_in_request_get(request, 'personAmt'))
        gender = check_in_request_get(request, 'gender')
        smoker = check_in_request_get(request,'smoker')
        servicios = check_in_request_get(request,'servicios')
        wifi = check_in_request_get(request, 'wifi')
        estacionamiento = check_in_request_get(request,'estacionamiento')
        limpieza = check_in_request_get(request, 'limpieza')
        gym = check_in_request_get(request,'gym')
        elevador = check_in_request_get(request,'elevador')
        bano = check_in_request_get(request, 'bano')
        facturacion = check_in_request_get(request, 'facturacion')
        cocina = check_in_request_get(request, 'cocina')
        comida = check_in_request_get(request, 'comida')
        mascotas = check_in_request_get(request, 'mascotas')
        visitas = check_in_request_get(request, 'visitas')
        infantes = check_in_request_get(request, 'infantes')
        lavadora = check_in_request_get(request, 'lavadora')
        secadora = check_in_request_get(request, 'secadora')
        directo = check_in_request_get(request, 'directo')
        # estado = check_in_request_get(request, 'estado')
        # municipio = check_in_request_get(request, 'municipio')
        # colonia = check_in_request_get(request, 'colonia')
        orden = check_in_request_get(request, 'sort')

        queryset = PostPerson.objects.all()

        queryset = queryset.filter(
            paused__exact = False
        )

        # Por ubicación

        queryset = queryset.filter(
            latitud__lte = (norte+1),
            latitud__gte = (sur-1),
            longitud__lte = (este+1),
            longitud__gte = (oeste-1)

        )

        #ORDEN (SORT) DE RESULTADOS

        if orden == 'precioMenor':
            queryset = queryset.all().order_by('price')
        
        if orden == 'precioMayor':
            queryset = queryset.all().order_by('-price')

        if minP >= 1:
            queryset = queryset.filter(
                price__gte = minP
            )

        if maxP >= 1:
            queryset = queryset.filter(
                price__lte = maxP
            )
        
        if personAmt != 0:
            queryset = queryset.filter(
                amount__lte = personAmt
            )

        if gender == 'mujer':
            queryset = queryset.filter(
                gender__exact='mujer'
            )
        elif gender == 'hombre':
            queryset = queryset.filter(
                gender__exact='hombre'
            )
        
        if smoker == 'on':
            queryset = queryset.filter(
                smokes__exact=False
            )

        if servicios == 'on':
            queryset = queryset.filter(
                amenities__icontains='servicios'
            )

        if wifi == 'on':
            queryset = queryset.filter(
                amenities__icontains='wifi'
            )
        
        if estacionamiento == 'on':
            queryset = queryset.filter(
                amenities__icontains='estacionamiento'
            )
        
        if limpieza == 'on':
            queryset = queryset.filter(
                amenities__icontains='limpieza'
            )
        
        if gym == 'on':
            queryset = queryset.filter(
                amenities__icontains='gym'
            )
        
        if elevador == 'on':
            queryset = queryset.filter(
                amenities__icontains='elevador'
            )
        
        if bano == 'on':
            queryset = queryset.filter(
                amenities__icontains='bano'
            )
        

        if facturacion == 'on':
            queryset = queryset.filter(
                amenities__icontains='facturacion'
            )

        if cocina == 'on':
            queryset = queryset.filter(
                amenities__icontains='cocina'
            )

        if comida == 'on':
            queryset = queryset.filter(
                amenities__icontains='comida'
            )
        
        if mascotas == 'on':
            queryset = queryset.filter(
                amenities__icontains='mascotas'
            )
        
        if visitas == 'on':
            queryset = queryset.filter(
                amenities__icontains='visitas'
            )

        if infantes == 'on':
            queryset = queryset.filter(
                amenities__icontains='infantes'
            )

        if lavadora == 'on':
            queryset = queryset.filter(
                amenities__icontains='lavadora'
            )
        
        if secadora == 'on':
            queryset = queryset.filter(
                amenities__icontains='secadora'
            )

        if directo == 'on':
            queryset = queryset.filter(
                amenities__icontains='directo'
            )
        
    p = Paginator(queryset, 50)
    page_num = request.GET.get('page',1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)


    context = {
            "persons": page,
            "request":request
            }


    if request.user.is_authenticated:
        userid = request.user.id
        profile = get_object_or_404(Profile, user=userid)
        favorites = profile.person_favorites.all()
        if favorites:
            context["favorites"] = favorites

    return render(request, "find/find_person.html",context)

