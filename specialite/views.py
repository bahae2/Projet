from django.shortcuts import render
from django.http import JsonResponse
from .models import Specialite, ChatbotResponse
import json
from django.views.decorators.csrf import csrf_exempt
import json
import google.generativeai as genai
from django.conf import settings
import logging
from .models import ChatbotResponse


def home(request):
    specialites = Specialite.objects.all()
    return render(request, 'specialite/home.html', {'specialites': specialites})

from django.shortcuts import render


def ia(request):
    specialite_ia = Specialite.objects.filter(nom="Intelligence Artificielle").first()
    return render(request, 'specialite/ia.html', {'specialite': specialite_ia})


from django.shortcuts import render


def securite(request):
    definitions = [
        {"titre": "Sécurité Informatique", "description": "Protéger les systèmes...", "video_url": "https://www.youtube.com/embed/XXXXX"},
        {"titre": "Cryptographie", "description": "Chiffrer les données...", "video_url": "https://www.youtube.com/embed/YYYYY"},
    ]
    return render(request, "specialite/securite.html", {"definitions": definitions, "video_path": "static/specialite/videos/vedio2.mp4"})


def reseau(request):
    return render(request, 'specialite/reseau.html')

def web(request):
    return render(request, 'specialite/web.html')











logger = logging.getLogger(__name__)

@csrf_exempt  # Désactiver en production
def chatbot_response(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            question = data.get("question", "").strip()

            if not question:
                return JsonResponse({"response": "Veuillez poser une question valide."}, status=400)

            response = ChatbotResponse.objects.filter(question__icontains=question).first()

            if response:
                return JsonResponse({"response": response.reponse})
            else:
                return JsonResponse({"response": "Je ne connais pas la réponse à cette question."})

        except json.JSONDecodeError:
            return JsonResponse({"response": "Format JSON invalide."}, status=400)
        except Exception as e:
            logger.error(f"Erreur serveur: {e}")
            return JsonResponse({"response": "Une erreur interne est survenue."}, status=500)

    return JsonResponse({"response": "Méthode non autorisée."}, status=405)

# Assure-toi d'avoir configuré ta clé API correctement
#import os
#GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
#genai.configure(api_key=GEMINI_API_KEY)
  # Assure-toi que ta clé est correcte

#def chatbot(request):
    model = genai.GenerativeModel("gemini-pro")
    
    response = model.generate_content("Bonjour, comment vas-tu ?")

    return JsonResponse({"response": response.text})