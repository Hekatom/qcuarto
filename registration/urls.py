from django.urls import path
from .views import SignUpView, LogoutView, DeleteView, confirm_delete_user, delete_user

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="account_signup"),
    path('logout/', LogoutView.as_view(), name="account_logout"),
    path('confirm_delete/<int:userid>/', confirm_delete_user, name="account_delete_confirm"),
    path('delete/<int:userid>/', delete_user, name="account_delete"),
    #path('sample/', SamplePageView.as_view(), name="sample"),
]