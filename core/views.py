from django.shortcuts import render
from django.views.generic.base import TemplateView
from posts.models import PostPerson, PostRoom
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    user_amt = User.objects.all().count()
    person_amt = PostPerson.objects.all().count()
    room_amt = PostRoom.objects.all().count()
    total_amt = person_amt + room_amt
    context = {
        "user_amt":user_amt,
        "person_amt":person_amt,
        "room_amt":room_amt,
        "total_amt":total_amt
    }
    
    
    return render(request,
                  'core/index.html',
                  context)


def handle_not_found(request, exception):
    return render(request,
                  'core/404.html')