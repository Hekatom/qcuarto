from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import TemplateView, DetailView
from django.urls import reverse_lazy
from posts.models import PostPerson, PostRoom
from django.contrib.auth.models import User

# Create your views here.
class SeenGeneralView(LoginRequiredMixin, TemplateView):
    template_name = "seen/seen_general.html"

class SeenPersonListView(LoginRequiredMixin, ListView):
    model = PostPerson
    template_name = "seen/seenperson_list.html"
        
    def my_persons(self):
        username = self.request.user.id
        persons = PostPerson.objects.filter(author=username)
        return persons

class SeenRoomListView(LoginRequiredMixin, ListView):
    model = PostRoom
    template_name = "seen/seenroom_list.html"
    
    def my_rooms(self):
        username = self.request.user.id
        rooms = PostRoom.objects.filter(author=username)
        return rooms
    
def person_removeseen(request,userid, personid):
    user = get_object_or_404(User,id=userid)
    person = get_object_or_404(PostPerson, id=personid)
    person.seen_by.remove(user)

    return redirect('profile', userid=userid) 


def room_removeseen(request,userid, roomid):
    user = get_object_or_404(User,id=userid)
    room = get_object_or_404(PostRoom, id=roomid)
    room.seen_by.remove(user)

    return redirect('profile', userid=userid) 
