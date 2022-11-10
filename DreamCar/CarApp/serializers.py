from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name','email', 'password', 'phone',
                  'gender', 'is_active', 'is_staff', 'is_superuser']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.times():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


class YearSerializer(serializers.ModelSerializer):

    class Meta:
        model = Year
        fields = ['id', 'year']


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ['id', 'year', 'time', 'about', 'model', 'topSpeed', 'torque', 'horsePower', 
                    'fuelType', 'seats', 'price', 'insurance', 'tank', 'img1', 'img2', 'img3', 'img4', 'img5']


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['id', 'user', 'name', 'phone', 'email',
                    'profilePic']


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ['id', 'pickupLocation', 'dropLocation']


class AdditionalsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Additionals
        fields = ['id', 'name', 'insurance', 'fuel']


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'customer', 'customerID', 'carModel', 'licenceID', 'price', 
                    'pickUP', 'fullFuel', 'insurance', 'payed']


class CancelledOrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = CancelledOrders
        fields = ['id', 'customerID', 'licenceID', 'price', 'payed']


class FaqSerializer(serializers.ModelSerializer):

    class Meta:
        model = Faq
        fields = ['id', 'title', 'content', 'question']