from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r'', UserViewset)


urlpatterns = [
    path('auth/', include(router.urls), name='authentication'),
    path('auth/login', signIN, name='logIn'),
    path('auth/logout/<int:pk>/', signOUT, name='logOut'),
    path('', CarListAPIView.as_view(), name='cars'),
    path('car/create/', CarCreateAPIView.as_view(), name='cars'),
    path('car/<int:pk>/', CarDetailAPIView.as_view(), name='car_details'),
    path('car/update/<int:pk>/', CarUpdateAPIView.as_view(), name='car_update'),
    path('car/delete/<int:pk>/', CarDeleteAPIView.as_view(), name='car_delete'),
    path('customer/create/', CustomerCreateAPIView.as_view(), name='customer_create'),
    path('customers/', CustomerListAPIView.as_view(), name='customers'),
    path('customer/<int:pk>/', CustomerDetailAPIView.as_view(), name='customer_details'),
    path('customer/update/<int:pk>/', CustomerUpdateAPIView.as_view(), name='customer_update'),
    path('customer/delete/<int:pk>/', CustomerDeleteAPIView.as_view(), name='customer_delete'),
    path('order/create/', OrderCreateAPIView.as_view(), name='order_create'),
    path('orders/', OrderListAPIView.as_view(), name='orders'),
    path('order/<int:pk>', OrderDetailAPIView.as_view(), name='order_detail'),
    path('order/update/<int:pk>/', OrderUpdateAPIView.as_view(), name='order_update'),
    path('order/delete/<int:pk>/', OrderDeleteAPIView.as_view(), name='order_delete'),
    path('cancel_order/', CreateOrderCancellation.as_view(), name='cancell_order'),
    path('cancelled_orders/', CancelledOrderListAPIView.as_view(), name='cancelled_orders'),
    path('cancelled_order/<int:pk>/', CancelledOrderDetailAPIView.as_view(), name='cancelled_order_details'),
    path('cancelled_order/update/<int:pk>/', CancelledOrderUpdateAPIView.as_view(), name='cancelled_order_update'),
    path('cancelled_order/delete/<int:pk>/', CancelledOrderDeleteAPIView.as_view(), name='cancelled_order_delete'),
]
