from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import TemplateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from registration.models import Profile
from posts.models import PostPerson, PostRoom

# Create your views here.
class FavGeneralView(LoginRequiredMixin, TemplateView):
    template_name = "favorites/fav_general.html"

class FavPersonView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = "favorites/favperson.html"

    def fav_people(self):
        userid = self.request.user.id
        profile = get_object_or_404(Profile, user=userid)
        people = profile.person_favorites.all()
        return people

class FavRoomView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = "favorites/favroom.html"

    def fav_rooms(self):
        userid = self.request.user.id
        profile = get_object_or_404(Profile, user=userid)
        rooms = profile.room_favorites.all()
        return rooms

def person_addfav(request,userid, personid):
    profile = get_object_or_404(Profile, user=userid)
    person = get_object_or_404(PostPerson, id=personid)
    profile.person_favorites.add(person)
    next=request.GET.get('next')
    print("Next:",next)
    if next!='':
        return redirect(next)
    else:
        return HttpResponse(status=204)

def room_addfav(request,userid, roomid):
    profile = get_object_or_404(Profile, user=userid)
    room = get_object_or_404(PostRoom, id=roomid)
    profile.room_favorites.add(room)
    next=request.GET.get('next')
    print("Next:",next)
    if next!='':
        return redirect(next)
    else:
        return HttpResponse(status=204)


def person_removefav(request,userid, personid):
    profile = get_object_or_404(Profile, user=userid)
    person = get_object_or_404(PostPerson, id=personid)
    profile.person_favorites.remove(person)
    next=request.GET.get('next')
    print("Next:",next)
    if next!='':
        return redirect(next)
    else:
        return HttpResponse(status=204)

def room_removefav(request,userid, roomid):
    profile = get_object_or_404(Profile, user=userid)
    room = get_object_or_404(PostRoom, id=roomid)
    profile.room_favorites.remove(room)
    next=request.GET.get('next')
    print("Next:",next)
    if next!='':
        return redirect(next)
    else:
        return HttpResponse(status=204)


#def room_removefav(request,userid, roomid):
#    user = get_object_or_404(User,id=userid)
#    room = get_object_or_404(PostRoom, id=roomid)
#    room.seen_by.remove(user)
#
#    return redirect('fav', userid=userid) 

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

