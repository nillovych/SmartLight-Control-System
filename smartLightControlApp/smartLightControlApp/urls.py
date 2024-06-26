from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authApp.urls')),
    path('profile/', include('profileApp.urls')),
    path('lights/', include('lightEntitiesControlApp.urls')),
]

