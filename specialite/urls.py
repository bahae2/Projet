from django.urls import path
from .views import home, ia, securite, reseau, web, chatbot_response

urlpatterns = [
    path('', home, name='home'),
    path('ia/', ia, name='ia'),
    path('securite/', securite, name='securite'),
    path('reseau/', reseau, name='reseau'),
    path('web/', web, name='web'),
    path('chatbot/', chatbot_response, name='chatbot_response'),
]
