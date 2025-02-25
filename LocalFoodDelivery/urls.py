"""
URL configuration for LocalFoodDelivery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from LocalFoodDelivery import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('',views.home, name="home"),
    path('produce/',views.produce_view, name="produce"),
    path('farmerlogin',views.farmerlogin, name="farmerlogin"),
    path('customerlogin',views.customerlogin, name="customerlogin"),
    path('farmer_dashboard',views.farmer_dashboard,name="farmer_dashboard"),
    path('customer_dashboard',views.customer_dashboard,name="customer_dashboard"),
    path('farmer',views.farmer,name="farmer"),
    path('customer',views.customer,name="customer"),
    path('vegetable',views.vegetable,name="vegetable"),
    path('leafygreens',views.leafygreens, name="leafygreens"),
    path('seasonalfruits',views.seasonalfruits, name="seasonalfruits"),
    path('rootvegetables',views.rootvegetables, name="rootvegetables"),
    path('dairyproduct',views.dairyproduct, name="dairyproduct"),
    path('summer',views.summer,name="summer"),
    path('autumn',views.autumn, name ="autumn"),
    path('winter',views.winter,name="winter"),
    path('spring',views.spring,name="spring"),
]
