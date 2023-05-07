from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    problem = models.TextField(max_length=300)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.name



class EventBooking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    event = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    duration = models.CharField(max_length=50)
    venue = models.TextField(max_length=200)
    address = models.TextField(max_length=200)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    guests = models.IntegerField()
    budget = models.BigIntegerField()
    catering = models.CharField(max_length=10)
    audioVisual = models.CharField(max_length=10)
    Photography = models.CharField(max_length=10)
    videography = models.CharField(max_length=10)
    decorations = models.CharField(max_length=10)
    other = models.TextField(max_length=2000)
    is_reads = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Admin(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    usertype = models.CharField(max_length=30) 
    pass1 = models.CharField(max_length=100)
    pass2 = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    forgot_password_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    

class Catering(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    servicetype = models.CharField(max_length=20)
    cateringtype = models.CharField(max_length=50)
    menuitems = models.CharField(max_length=50)
    dietres = models.CharField(max_length=50)


    def __str__(self):
        return self.name
    

class Photography(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    servicetype = models.CharField(max_length=20)
    photographytype = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    style = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    delivery = models.CharField(max_length=50)
    additional = models.CharField(max_length=50)

    def __str__(self):
        return self.name





class AudioVisuals(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    servicetype = models.CharField(max_length=30)
    equipment = models.CharField(max_length=30)
    avquantity = models.CharField(max_length=30)
    techsupp = models.CharField(max_length=30)

    def __str__(self):
        return self.name



class Videography(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    servicetype = models.CharField(max_length=30)
    vivideography = models.CharField(max_length=30)
    viduration = models.CharField(max_length=30)
    vistyle = models.CharField(max_length=30)
    vilocation = models.CharField(max_length=30)
    videlivery = models.CharField(max_length=30)
    viadditional = models.CharField(max_length=30)


    def __str__(self):
        return self.name


class Decoration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    servicetype = models.CharField(max_length=30)
    dedecoration = models.CharField(max_length=30)

    def __str__(self):
        return self.name
