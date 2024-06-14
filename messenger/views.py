from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import TemplateView, DetailView
from django.urls import reverse_lazy
from .models import Thread,Message
from django.contrib.auth.models import User
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.
class ThreadList(LoginRequiredMixin,TemplateView):
    template_name="messenger/messages.html"    

class ThreadDetail(LoginRequiredMixin,DetailView):
    model = Thread
    template_name="messenger/chat.html"

    def get_object(self):
        obj = super(ThreadDetail, self).get_object()
        if self.request.user not in obj.users.all():
            raise Http404
        return obj

@login_required
def start_thread(request, userid):
    user = get_object_or_404(User, id=userid)
    thread = Thread.objects.find_or_create(user, request.user)
    return redirect(reverse_lazy('chat', args=[thread.pk]))

@login_required
def add_message(request, pk):
    jsr = {'created':False}
    if request.user.is_authenticated:
        content = request.GET.get("content", None)
        if content:
            thread = get_object_or_404(Thread, pk=pk)
            message = Message.objects.create(user=request.user, content=content)
            thread.messages.add(message)
            jsr['created'] = True
    else:
        raise Http404("User not authenticated.")
    return JsonResponse(jsr)