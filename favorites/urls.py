from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import FavGeneralView, FavRoomView, FavPersonView
from .views import person_removefav, room_removefav, person_addfav, room_addfav
#from .views import room_removefav, person_removefav

urlpatterns = [
    path('',login_required(FavGeneralView.as_view()),name="fav"),
    path('rooms/',login_required(FavRoomView.as_view()),name="fav_room"),
    path('people/',login_required(FavPersonView.as_view()),name="fav_person"),
    path('room_removefav/<int:userid>/<int:roomid>/', login_required(room_removefav), name='room_removefav'),
    path('person_removefav/<int:userid>/<int:personid>/', login_required(person_removefav), name='person_removefav'),
    path('room_addfav/<int:userid>/<int:roomid>/', login_required(room_addfav), name='room_addfav'),
    path('person_addfav/<int:userid>/<int:personid>/', login_required(person_addfav), name='person_addfav')
]