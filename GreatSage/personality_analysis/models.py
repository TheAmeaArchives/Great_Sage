from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class TextAnalysis(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    text = models.TextField()
    created_at =  models.DateTimeField(auto_now_add=True)
    results = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.user} wrote {self.text[0:20]}"
    
class HandwritingAnalysis(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    handwriting_image = models.ImageField(upload_to= 'handwriting_samples/')
    created_at =  models.DateTimeField(auto_now_add=True)
    results = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.user} handwriting"
    
class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    created_at =  models.DateTimeField(auto_now_add=True)

class SoundtrackAnalysis(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    sound_text = models.TextField()
    created_at =  models.DateTimeField(auto_now_add=True)
    results = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.user} soundtrack"