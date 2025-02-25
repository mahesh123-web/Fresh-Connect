from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('farmer/', views.farmer, name='farmer'),
    path('customer/', views.customer, name='customer'),
    # path('admin/', admin.site.urls),
    # path('users/', include('users.urls')),
]