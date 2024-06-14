from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
#from .forms import RegistrationForm
from django.views.generic import CreateView, TemplateView, DeleteView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.http import HttpResponse
from core.views import index


# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'

    def get_success_url(self):
        URL = self.request.GET.get('next')
        return URL

class LogoutView(TemplateView):
    template_name = "registration/logout.html"

    def get_success_url(self):
        URL = self.request.GET.get('next')
        return URL

class DeleteUser(DeleteView):
    model = User
    template_name = 'registration/delete.html'
    success_url = reverse_lazy('home')

def confirm_delete_user(request, userid):
    template_name = 'registration/delete.html'

    return render(request, template_name)


def delete_user(request, userid):

    try:
        user = User.objects.get(id=userid)
        user.delete()
        return render(request, index)
    except Exception as e: 
        return HttpResponse('Algo salió mal')


