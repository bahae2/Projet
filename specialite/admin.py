from django.contrib import admin
# Register your models here.
from .models import Specialite
from django.contrib import admin
from .models import ChatbotResponse

admin.site.register(ChatbotResponse)
admin.site.register(Specialite)
