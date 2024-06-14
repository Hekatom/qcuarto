from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import FindGeneralView, room_results, person_results


urlpatterns = [
    path('',FindGeneralView.as_view(),name="find"),
    # path('room/',room_results,name="room_results"),
    path('room/',room_results,name="find_room"),
    #path('room/',RoomSearchView.as_view(),name="search_room"),
    path('person/',person_results,name="find_person"),
    ]