from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name="home"),
    #path('sample/', SamplePageView.as_view(), name="sample"),
]