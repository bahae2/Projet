from django.contrib import admin
from django.urls import path, include
from specialite import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Ajout de la virgule ici
    path('', include('specialite.urls')),  # Modification de l'URL pour éviter les conflits
]

