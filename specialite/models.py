from django.db import models

# Create your models here.

class Specialite(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    video_url = models.URLField()
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.nom

class ChatbotResponse(models.Model):
    question = models.CharField(max_length=255)
    reponse = models.TextField()  # Assure-toi que ce champ existe bien

    def __str__(self):
        return self.question


