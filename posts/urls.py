from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import PersonSubmitCreateView, RoomSubmitCreateView, PostsGeneralView, PostPersonListView, PostRoomListView, RoomDetailView, PersonDetailView, RoomUpdateView, PersonUpdateView, RoomDeleteView, PersonDeleteView
from .views import room_pause, person_pause, contact
urlpatterns = [
    path('person_submit/', login_required(PersonSubmitCreateView.as_view()), name="person_submit"),
    path('room_submit/',login_required(RoomSubmitCreateView.as_view()),name="room_submit"),
    path('my_posts/',login_required(PostsGeneralView.as_view()),name="posts_general"),
    path('my_rooms/',login_required(PostRoomListView.as_view()),name="room_list"),
    path('my_persons/',login_required(PostPersonListView.as_view()),name="person_list"),
    path('room/<int:pk>/<slug:slug>/', RoomDetailView.as_view(), name='room'),
    path('person/<int:pk>/<slug:slug>/', PersonDetailView.as_view(), name='person'),
    path('room/update/<int:pk>/', RoomUpdateView.as_view(), name='room_update'),
    path('person/update/<int:pk>/', PersonUpdateView.as_view(), name='person_update'),
    path('person_delete/<int:pk>/', PersonDeleteView.as_view(), name='person_delete'),
    path('room_delete/<int:pk>/', RoomDeleteView.as_view(), name='room_delete'),
    path('room_pause/<int:pk>/', room_pause, name='room_pause'),
    path('person_pause/<int:pk>/', person_pause, name='person_pause'),
    path('contact/<str:type>/<int:pk>/', contact, name='contact')  
]

