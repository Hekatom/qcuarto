from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField 
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
import os
from registration.models import Profile
from PIL import Image
from datetime import datetime


def person_img_name(instance,filename):
    picname = filename.split('.')[0]
    ext = filename.split('.')[-1]
    userid = instance.author.id
    filename = "%s_%s.%s" % (picname,userid,ext)
    return os.path.join('posts/PersonPosts/', filename)


class PostPerson(models.Model): 
      
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=1,related_name='person_author')
    account = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='person_profile',default=1)
    # colonia = models.ForeignKey(Colonia, on_delete=models.SET_NULL, blank=True, null=True)
    # cp = models.ForeignKey(CP, on_delete=models.SET_NULL, blank=True, null=True)
    # municipio = models.ForeignKey(Municipio, on_delete=models.SET_NULL, blank=True, null=True)
    # estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, blank=True, null=True)
    latitud = models.DecimalField(max_digits=20, decimal_places=16, null=False, blank=False, default=0.0)
    longitud = models.DecimalField(max_digits=20, decimal_places=16, null=False, blank=False, default=0.0)
    image = models.ImageField(upload_to=person_img_name,null=True, blank=True)
    name = models.CharField(max_length=100,null=False,blank=False)
    description = models.TextField(max_length=350,null=False,blank=True)
    gender = models.CharField(max_length=100, null=False,blank=False)
    smokes = models.BooleanField(default=False,null=False,blank=False)
    amount = models.PositiveIntegerField(default=1,null=False,blank=False)
    amenities = models.CharField(max_length=900, default=1)
    phone = PhoneNumberField(blank=False)
    whatsapp = models.BooleanField(default=False, null=False, blank=False)
    price = models.PositiveIntegerField(null=False,blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    last_seen = models.DateTimeField(auto_now=True)
    visits = models.IntegerField(default=0, null=True, blank = True)
    contacts = models.IntegerField(default=0, null=True, blank = True)
    paused = models.BooleanField(default=False, null=False, blank=False)
    blocked = models.BooleanField(default=False, null=False, blank=False)
    seen_by = models.ManyToManyField(User,related_name='person_seen_by', blank=True)
    featured = models.BooleanField(default=False, null=False, blank=False)
    verified = models.BooleanField(default=False, null=False, blank=False)

    def add_visit(self):
        if self.visits is not None:
            self.visits += 1
        else:
            self.visits += 0

    def add_update(self):
        self.updated = datetime.now()

# @receiver(post_save, sender=PostPerson)
# def person_created(sender, instance, **kwargs):
#     if kwargs.get('created', True):
#         col = instance.colonia
#         cpcol = col.cp
#         cpid = cpcol.id
#         instance.cp = CP.objects.get(id=cpid)

@receiver(pre_save, sender=PostPerson)
def person_account(sender, instance, **kwargs):
    author = instance.author
    object = Profile.objects.get(user=author)
    print("person perfil:",object)
    instance.account = object
    print("person account:",instance.account)

@receiver(post_save, sender=PostPerson)
def person_image(sender, instance,**kwargs):
    pic = Image.open(instance.image.path)
    pic.save(instance.image.path,quality=35,optimize=True)


def room_img1_name(instance,filename):
    picname = filename.split('.')[0]
    ext = filename.split('.')[-1]
    userid = instance.author.id
    filename = "%s_%s_%s.%s" % (picname,userid,"1",ext)
    return os.path.join('posts/RoomPosts/', filename)

def room_img2_name(instance,filename):
    picname = filename.split('.')[0]
    ext = filename.split('.')[-1]
    userid = instance.author.id
    filename = "%s_%s_%s.%s" % (picname,userid,"2",ext)
    return os.path.join('posts/RoomPosts/', filename)

def room_img3_name(instance,filename):
    picname = filename.split('.')[0]
    ext = filename.split('.')[-1]
    userid = instance.author.id
    filename = "%s_%s_%s.%s" % (picname,userid,"3",ext)
    return os.path.join('posts/RoomPosts/', filename)

def room_img4_name(instance,filename):
    picname = filename.split('.')[0]
    ext = filename.split('.')[-1]
    userid = instance.author.id
    filename = "%s_%s_%s.%s" % (picname,userid,"4",ext)
    return os.path.join('posts/RoomPosts/', filename)

def room_img5_name(instance,filename):
    picname = filename.split('.')[0]
    ext = filename.split('.')[-1]
    userid = instance.author.id
    filename = "%s_%s_%s.%s" % (picname,userid,"5",ext)
    return os.path.join('posts/RoomPosts/', filename)

def room_img6_name(instance,filename):
    picname = filename.split('.')[0]
    ext = filename.split('.')[-1]
    userid = instance.author.id
    filename = "%s_%s_%s.%s" % (picname,userid,"6",ext)
    return os.path.join('posts/RoomPosts/', filename)


class PostRoom(models.Model):
      
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=1,related_name='room_author')
    account = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='room_profile',default=1)
    # colonia = models.ForeignKey(Colonia, on_delete=models.SET_NULL, blank=True, null=True)
    # cp = models.ForeignKey(CP, on_delete=models.SET_NULL, blank=True, null=True)
    # municipio = models.ForeignKey(Municipio, on_delete=models.SET_NULL, blank=True, null=True)
    # estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, blank=True, null=True)
    latitud = models.DecimalField(max_digits=20, decimal_places=16, null=False, blank=False, default=0.0)
    longitud = models.DecimalField(max_digits=20, decimal_places=16, null=False, blank=False, default=0.0)
    image1 = models.ImageField(upload_to=room_img1_name,null=True, blank=True)
    image2 = models.ImageField(upload_to=room_img2_name,null=True, blank=True)
    image3 = models.ImageField(upload_to=room_img3_name,null=True, blank=True)
    image4 = models.ImageField(upload_to=room_img4_name,null=True, blank=True)
    image5 = models.ImageField(upload_to=room_img5_name,null=True, blank=True)
    image6 = models.ImageField(upload_to=room_img6_name,null=True, blank=True)
    title = models.CharField(max_length=120,null=False,blank=False)
    description = models.TextField(max_length=400,null=False,blank=True)
    gender = models.CharField(max_length=100, null=False,blank=False)
    place = models.CharField(max_length=100, null=False,blank=False)
    smokers = models.CharField(max_length=100, null=False,blank=False)
    several = models.BooleanField(default=False,null=False,blank=False)
    min_amount = models.PositiveIntegerField(default=1,null=False,blank=False)
    max_amount = models.PositiveIntegerField(default=1,null=False,blank=False)
    price_extra = models.PositiveIntegerField(default=0,null=False,blank=True)
    amenities = models.CharField(max_length=900, default=1)
    phone = PhoneNumberField(blank=False)
    whatsapp = models.BooleanField(default=False, null=False, blank=False)
    price = models.PositiveIntegerField(null=False,blank=False)
    deposit_check = models.BooleanField(default=False,null=False,blank=False)
    deposit_amount = models.PositiveIntegerField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    last_seen = models.DateTimeField(auto_now=True)
    visits = models.IntegerField(default=0, null=True, blank = True)
    contacts = models.IntegerField(default=0, null=True, blank = True)
    paused = models.BooleanField(default=False, null=False, blank=False)
    blocked = models.BooleanField(default=False, null=False, blank=False)
    seen_by = models.ManyToManyField(User,related_name='room_seen_by', blank=True)
    featured = models.BooleanField(default=False, null=False, blank=False)
    verified = models.BooleanField(default=False, null=False, blank=False)

    def add_visit(self):
        if self.visits is not None:
            self.visits += 1
        else:
            self.visits += 0

    def add_update(self):
        self.updated = datetime.now()
    
# @receiver(post_save, sender=PostRoom)
# def room_created(sender, instance, **kwargs):
#     if kwargs.get('created', True):
#         col = instance.colonia
#         if col != None:
#             cpcol = col.cp
#             cpid = cpcol.id
#             instance.cp = CP.objects.get(id=cpid)
#         else:
#             pass

@receiver(pre_save, sender=PostRoom)
def room_account(sender, instance, **kwargs):
    author = instance.author
    object = Profile.objects.get(user=author)
    print("room perfil:",object)
    instance.account = object
    print("room account:",instance.account)

@receiver(post_save, sender=PostRoom)
def room_image(sender, instance,**kwargs):
    if instance.image1:
        pic1 = Image.open(instance.image1.path)
        pic1.save(instance.image1.path,quality=35,optimize=True)
    if instance.image2:
        pic2 = Image.open(instance.image2.path)
        pic2.save(instance.image2.path,quality=35,optimize=True)
    if instance.image3:
        pic3 = Image.open(instance.image3.path)
        pic3.save(instance.image3.path,quality=35,optimize=True)
    if instance.image4:
        pic4 = Image.open(instance.image4.path)
        pic4.save(instance.image4.path,quality=35,optimize=True)
    if instance.image5:
        pic5 = Image.open(instance.image5.path)
        pic5.save(instance.image5.path,quality=35,optimize=True)
    if instance.image6:
        pic6 = Image.open(instance.image6.path)
        pic6.save(instance.image6.path,quality=35,optimize=True)
 
    


 