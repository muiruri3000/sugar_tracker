
from django.contrib import admin
from django.urls import path,include
from login.views import home
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),
    path('', lambda request: redirect('home')),
]