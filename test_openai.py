import openai
import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis .env
load_dotenv()

# Récupérer la clé API stockée dans .env
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Erreur : Clé API OpenAI introuvable dans .env")
    exit()

# Initialiser le client OpenAI
client = openai.OpenAI(api_key=api_key)

try:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Bonjour, comment vas-tu ?"}]
    )
    print("Réponse OpenAI:", response.choices[0].message.content)
except openai.OpenAIError as e:
    print("Erreur OpenAI:", e)
