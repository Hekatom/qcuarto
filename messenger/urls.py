from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ThreadList,ThreadDetail, start_thread, add_message

urlpatterns = [
    path('', login_required(ThreadList.as_view()), name="messages"),
    path('chat/<int:pk>', login_required(ThreadDetail.as_view()), name="chat"),
    path('chat/start/<userid>/', start_thread, name="start_chat"),
    path('chat/<int:pk>/add/', add_message, name="add_message"),

]