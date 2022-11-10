from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    first_name = models.CharField(max_length=175)
    last_name = models.CharField(max_length=175)
    username = models.CharField(max_length=250, unique=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    phone = models.CharField(max_length=12, blank=True, null=True)
    gender = models.CharField(max_length=11, blank=True, null=True)
    session_token = models.CharField(max_length=35, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.email}'


class Year(models.Model):

    year = models.CharField(max_length=4, unique=True)

    def __str__(self):
        return self.year


class Car(models.Model):

    year = models.ForeignKey(Year, on_delete = models.CASCADE, null=True)
    time = models.IntegerField(null = True, blank=True)
    about = models.TextField(max_length = 500, null=True, blank=True)
    model = models.CharField(max_length=120, null=True, blank=True)
    topSpeed = models.IntegerField(null=True, blank=True)
    torque = models.IntegerField(null=True, blank=True)
    horsePower = models.IntegerField(null=True, blank=True)
    fuelType = models.CharField(max_length=12, null=True, blank=True)
    seats = models.IntegerField(null=True, blank=True)
    price = models.CharField(max_length=10, null=True, blank=True)
    insurance = models.IntegerField(null=True, blank=True)
    tank = models.IntegerField(null=True, blank=True)
    img1 = models.ImageField(null=True)
    img2 = models.ImageField(null=True)
    img3 = models.ImageField(null=True)
    img4 = models.ImageField(null=True)
    img5 = models.ImageField(null=True)

    def __Str__(self):
        return f'{self.model} - {self.fuelType} - {self.price}'


class Customer(models.Model):

    user = models.OneToOneField(User, null=True, on_delete = models.CASCADE)
    name = models.CharField(max_length=125, null=True)
    phone = models.CharField(max_length=12, null=True)
    email = models.EmailField(max_length=25, null=True)
    createdOn = models.DateTimeField(auto_now_add=True, null=True)
    profilePic = models.ImageField(null=True, blank=True) 

    def __str__(self):
        return f'{self.name} - {self.phone} - {self.email}'


class Location(models.Model):

    pickUpLocation = models.CharField(max_length=150, null=True)
    dropLocation = models.CharField(max_length=150, null=True)

    
    def __str__(self):
        return f'{self.pickUpLocation} - {self.dropLocation}'


class Additionals(models.Model):

    name = models.CharField(max_length=120, null=True)
    insurance = models.IntegerField(null=True, blank=True)
    fuel = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):

    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    customerID = models.CharField(max_length=50, null=True)
    carModel = models.CharField(max_length=70, null=True)
    licenceID = models.CharField(null=True, max_length=10)
    price = models.IntegerField(null=True, blank=False)
    rentNow = models.DateField(auto_now_add=False, null=True)
    finishNow = models.DateField(auto_now_add=False, null=True)
    orderDate = models.DateTimeField(auto_now_add=True, null=True)
    pickUP = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    fullFuel = models.BooleanField(blank=True, null=True, default=False)
    insurance = models.BooleanField(blank=True, null=True, default=False)
    payed = models.BooleanField(null=True, default=False)

    def __str__(self):
        return f'{self.customerID} - {self.price} - {self.payed}'


class CancelledOrders(models.Model):
    
    customerID = models.CharField(max_length=50, null=True)
    licenceID = models.CharField(null=True, max_length=10)
    price = models.IntegerField(null=True, blank=False)
    payed = models.BooleanField(null=True, default=False)

    def __str__(self):
        return f'{self.customerID} - {self.price} - {self.payed}'


class Faq(models.Model):

    title = models.CharField(max_length=35, null=True)
    content = models.TextField(max_length=500, null=True, blank=True)
    question = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'{self.title} - {self.question}'