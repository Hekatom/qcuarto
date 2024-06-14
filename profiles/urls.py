from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ProfileDetailView

urlpatterns = [
    #path('<int:pk>', login_required(ProfileView.as_view()), name="profile"),
    path('<int:userid>/', ProfileDetailView.as_view(), name="profile"),
    ]