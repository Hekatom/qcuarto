from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db import models
#from posts.models import PostRoom,PostPerson

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile_user')
    verified = models.BooleanField(default=False,null=False,blank=False)
    subscription = models.BooleanField(default=False,null=False,blank=False)
    room_favorites = models.ManyToManyField('posts.PostRoom', blank=True)
    person_favorites = models.ManyToManyField('posts.PostPerson', blank=True)
    link = models.URLField(max_length=200,null=True, blank=True)

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
	if kwargs.get('created', False):
		Profile.objects.get_or_create(user=instance) 
