import re
from django.contrib.auth import get_user_model, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.generics import (
    ListAPIView, CreateAPIView,
    RetrieveAPIView, DestroyAPIView,
    RetrieveUpdateAPIView
)
from rest_framework.permissions import (
    AllowAny, IsAuthenticated, 
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)
from .models import *
from .serializers import *


@csrf_exempt
def signIN(request):

    if request.method == 'POST':
        username = request.data.get('email')
        password = request.data.get('password')
        if not re.match("^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", username):
            return JsonResponse({'error': 'Please enter a valid EMAIL'})
        if len(password) < 6:
            return JsonResponse({'error' : 'Password must be atleast 5 char long'})
        
        UserModel = get_user_model()

        try:
            user = UserModel.objects.get(email = username)
            if user.check_password(password):
                get_user = UserModel.objects.filter(email = username).values().first()
                get_user.pop('password')
                user.save()
                login(request=request, user=user)
            else:
                return JsonResponse({'error' : 'Invalid Password'})
        except:
            return JsonResponse({'error': 'Invalid Email'})
    return JsonResponse({'error': 'Method not allowed!'})


@csrf_exempt
def signOUT(request, id):

    logout(request)
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk = id)
        user.session_token = '0'
        user.save()
    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Invalid user'})
    return JsonResponse({'Success': 'Susscessfully Logged Out'})


class UserViewset(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer

    def get_permission(self):
        permission_class = []
        if self.action == 'create' or self.action == 'reterive':
            permission_class = [AllowAny]
        elif self.action == 'reterive' or self.action == 'update' or self.action == 'partial_update':
            permission_class = [IsAuthenticated]
        elif self.action == 'list' or self.action == 'destroy':
            permission_class = [IsAdminUser]
        return [permission() for permission in permission_class]


class CarListAPIView(ListAPIView):

    queryset = Car.objects.all().order_by('-id')
    serializer_class = CarSerializer
    permission_classes = [AllowAny]


class CarCreateAPIView(CreateAPIView):

    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAdminUser]


class CarUpdateAPIView(RetrieveUpdateAPIView):

    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAdminUser]


class CarDetailAPIView(RetrieveAPIView):

    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarDeleteAPIView(DestroyAPIView):

    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAdminUser]


class CustomerCreateAPIView(CreateAPIView):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [AllowAny]


class CustomerListAPIView(ListAPIView):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]


class CustomerDetailAPIView(RetrieveAPIView):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]


class CustomerUpdateAPIView(RetrieveUpdateAPIView):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]


class CustomerDeleteAPIView(DestroyAPIView):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    
class OrderCreateAPIView(CreateAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


class OrderListAPIView(ListAPIView):

    queryset = Order.objects.all().order_by('-customerID')
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class OrderDetailAPIView(RetrieveAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class OrderUpdateAPIView(RetrieveUpdateAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]


class OrderDeleteAPIView(DestroyAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]


class CreateOrderCancellation(CreateAPIView):

    queryset = CancelledOrders.objects.all()
    serializer_class = CancelledOrdersSerializer
    permission_classes = [IsAuthenticated]


class CancelledOrderListAPIView(ListAPIView):

    queryset = CancelledOrders.objects.all().order_by('-id')
    serializer_class = CancelledOrdersSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class CancelledOrderDetailAPIView(RetrieveAPIView):

    queryset = CancelledOrders.objects.all()
    serializer_class = CancelledOrdersSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class CancelledOrderUpdateAPIView(RetrieveUpdateAPIView):

    queryset = CancelledOrders.objects.all()
    serializer_class = CancelledOrdersSerializer
    permission_classes = [IsAdminUser]


class CancelledOrderDeleteAPIView(DestroyAPIView):

    queryset = CancelledOrders.objects.all()
    serializer_class = CancelledOrdersSerializer
    permission_classes = [IsAdminUser]


