from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import SeenGeneralView, SeenRoomListView, SeenPersonListView
from .views import room_removeseen, person_removeseen

urlpatterns = [
    path('',login_required(SeenGeneralView.as_view()),name="seen"),
    path('rooms/',login_required(SeenRoomListView.as_view()),name="seen_room"),
    path('persons/',login_required(SeenPersonListView.as_view()),name="seen_person"),
    path('room_removeseen/<int:userid>/<int:roomid>/', login_required(room_removeseen), name='room_removeseen'),
    path('person_removeseen/<int:userid>/<int:personid>/', login_required(person_removeseen), name='person_removeseen')
    #path('<int:pk>/<slug:slug>/', RoomDetailView.as_view(), name='room'),
    #path('<int:pk>/<slug:slug>/', PersonDetailView.as_view(), name='person'),
]