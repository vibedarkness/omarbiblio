
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tacos/',include('main.urls')),
]


#URLS PROJET