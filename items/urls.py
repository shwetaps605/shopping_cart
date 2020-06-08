from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('details/<str:pk>/',views.detailed,name="details"),
    path('buy/<str:pk>/',views.buyItem,name="buy-portal"),
    path('checkout/<str:pk>/',views.checkout,name="checkout")
]