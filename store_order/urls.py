from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('order/', include('order.urls')),
    path('store/', include('store.urls')),
    path('', index),
]
