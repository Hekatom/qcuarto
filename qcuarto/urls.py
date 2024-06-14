"""qcuarto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings

urlpatterns = [
	# Paths del Core 
	# path('core/', include('core.urls')),
	path('', include('core.urls')),
    # Paths de XXXXX
    #path('XXXXX/', include('XXXXX.urls')),
    # Paths del Admin
    path('admin/', admin.site.urls),
    # Paths del Auth
    path('accounts/', include('allauth.urls')),
    # Paths de Registration
    path('accounts/', include('registration.urls')),
    # Paths de Posts
    path('posts/', include('posts.urls')),
    # Paths de Estaticas
    path('info/', include('estaticas.urls')),
    # Paths de Seen_by
    path('seen/', include('seen.urls')),
    # Paths de profiles
    path('profile/', include('profiles.urls')),
    # Paths de messenger
    path('messages/', include('messenger.urls')),
    # Paths de favoritos
    path('favorites/', include('favorites.urls')),
    # Paths de find
    path('find/', include('find.urls')),
    ]

# add a flag for
# handling the 404 error
handler404 = 'core.views.handle_not_found'

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
