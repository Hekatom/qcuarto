from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from registration.models import Profile
from posts.models import PostRoom, PostPerson
from django.contrib.auth.models import User

# Create your views here.
class ProfileDetailView(DetailView):
	model = Profile
	template_name = 'profiles/profile.html'

	def get_object(self):
		return get_object_or_404(Profile, user__id=self.kwargs['userid'])
	
	def profile_rooms(self):
		userid = get_object_or_404(User, id=self.kwargs['userid'])
		rooms = PostRoom.objects.filter(author=userid)
		return rooms

	def profile_persons(self):
		userid = get_object_or_404(User, id=self.kwargs['userid'])
		persons = PostPerson.objects.filter(author=userid)
		return persons

	def profile_posts(self):
		userid = get_object_or_404(User, id=self.kwargs['userid'])
		rooms = PostRoom.objects.filter(author=userid)
		persons = PostPerson.objects.filter(author=userid)
		total = len(persons) + len(rooms)
		return total
