from django.contrib import admin
from .models import PostPerson, PostRoom

# Register your models here.

admin.site.register(PostPerson)

admin.site.register(PostRoom)

class RoomAdmin(admin.ModelAdmin):
    search_fields = ['colonia__colonia']    

# from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin
# from .models import PostPerson, PostRoom

# # Register your models here.
# @admin.register(PostPerson)
# class PersonAdmin(ImportExportModelAdmin):
#     list_display = ('author','estado','municipio','colonia','image','name','description','gender','smokes','amount',
#                     'amenities', 'phone', 'price', 'updated', 'visits', 'contacts', 'paused', 'blocked',
#                     'seen_by','featured')

# @admin.register(PostPerson)
# class RoomAdmin(ImportExportModelAdmin):
#     list_display = ('author','estado','municipio','colonia','title','image1','description','gender','place','smokers',
#                     'several', 'min_amount', 'max_amount', 'price_extra', 'amenities', 'phone', 'price', 'deposit_check',
#                     'deposit_amount','updated', 'visits', 'contacts', 'paused', 'blocked',
#                     'seen_by','featured')