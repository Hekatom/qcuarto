from typing import Any, Dict
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import TemplateView, DetailView
from django.urls import reverse_lazy
from .models import PostPerson, PostRoom
from .forms import PostPersonForm, PostRoomForm
from django.contrib.auth.models import User
from registration.models import Profile
from django.core.exceptions import PermissionDenied

class RoomSubmitCreateView(LoginRequiredMixin, CreateView):
    model = PostRoom
    form_class = PostRoomForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)        
    success_url = reverse_lazy('room_list')



class PersonSubmitCreateView(LoginRequiredMixin, CreateView):
    model = PostPerson
    form_class = PostPersonForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    success_url = reverse_lazy('person_list')

class PostsGeneralView(LoginRequiredMixin, TemplateView):
    template_name = "posts/posts_general.html"

class PostPersonListView(LoginRequiredMixin, ListView):
    model = PostPerson
        
    def my_persons(self):
        userid = self.request.user.id
        persons = PostPerson.objects.filter(author=userid)
        return persons

class PostRoomListView(LoginRequiredMixin, ListView):
    model = PostRoom
    
    def my_rooms(self):
        userid = self.request.user.id
        rooms = PostRoom.objects.filter(author=userid)
        return rooms

class RoomDetailView(DetailView):
    model = PostRoom
    
    def get_context_data(self, **kwargs):
        context = super(RoomDetailView, self).get_context_data(**kwargs)
        self.object.add_visit()
        self.object.save()
        if self.request.user.is_authenticated and self.request.user != self.object.author:
            self.object.seen_by.add(self.request.user)
        if self.request.user.is_authenticated:
            #Perfil del usuario actual:
            userid = self.request.user
            profile = Profile.objects.get(user=userid)
            roomfav = profile.room_favorites.all()
            context['roomfav']=roomfav
        print(context)
        return context
    
    
    

class PersonDetailView(DetailView):
    model = PostPerson
    
    def get_context_data(self, **kwargs):
        context = super(PersonDetailView, self).get_context_data(**kwargs)
        self.object.add_visit()
        self.object.save()
        if self.request.user.is_authenticated and self.request.user != self.object.author:
            self.object.seen_by.add(self.request.user)
        if self.request.user.is_authenticated:
            #Perfil del usuario actual:
            userid = self.request.user
            profile = Profile.objects.get(user=userid)
            personfav = profile.person_favorites.all()
            context['personfav']=personfav
        return context

class RoomUpdateView(LoginRequiredMixin, UpdateView):
    model = PostRoom
    form_class = PostRoomForm
    success_url = reverse_lazy('room_list')

    def dispatch(self, request, *args, **kwargs):
        handler = super().dispatch(request, *args, **kwargs)
        user = request.user
        post = self.get_object()
        if not (post.author == user or user.is_superuser):
            raise PermissionDenied
        return handler
    
    def get_context_data(self, **kwargs):
        context = super(RoomUpdateView, self).get_context_data(**kwargs)
        room_data = self.object
        context['room_data']=room_data
        return context

class PersonUpdateView(LoginRequiredMixin, UpdateView):
    model = PostPerson
    form_class = PostPersonForm
    success_url = reverse_lazy('room_list')

    def dispatch(self, request, *args, **kwargs):
        handler = super().dispatch(request, *args, **kwargs)
        user = request.user
        post = self.get_object()
        if not (post.author == user or user.is_superuser):
            raise PermissionDenied
        return handler
    
    def get_context_data(self, **kwargs):
        context = super(PersonUpdateView, self).get_context_data(**kwargs)
        person_data = self.object
        context['person_data']=person_data
        return context

class RoomDeleteView(LoginRequiredMixin, DeleteView):
    model = PostRoom
    success_url = reverse_lazy('room_list')

class PersonDeleteView(LoginRequiredMixin, DeleteView):
    model = PostPerson
    success_url = reverse_lazy('person_list')

def room_pause(request, pk):
    room = get_object_or_404(PostRoom, pk=pk)
    if room.paused == True:
        room.paused = False
    elif room.paused == False:
        room.paused = True
    room.save(update_fields=['paused'])
    return redirect('room_list')

def person_pause(request, pk):
    person = get_object_or_404(PostPerson, pk=pk)
    if person.paused == True:
        person.paused = False
    elif person.paused == False:
        person.paused = True
    person.save(update_fields=['paused'])
    return redirect('person_list')

def contact(request,type,pk):
    if type=="room":
        post = get_object_or_404(PostRoom, pk=pk)
    elif type == "person":
        post = get_object_or_404(PostPerson, pk=pk)
    post.contacts += 1
    post.save()
    print("Contacto de",type,"con id:",pk)
    next=request.GET.get('next')
    print("Next:",next)
    if next!='':
        return redirect(next)
    else:
        return HttpResponse(status=204)


