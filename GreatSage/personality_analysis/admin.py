from django.contrib import admin
from .models import TextAnalysis, HandwritingAnalysis,Chat
# Register your models here.

@admin.register(TextAnalysis)
class TextAnalysisAdmin(admin.ModelAdmin):
    list_display=("user", "text", "created_at", "results")

@admin.register(HandwritingAnalysis)
class HandwritingAnalysisAdmin(admin.ModelAdmin):
    list_display=("user", "handwriting_image", "created_at", "results")

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ("user","message","response","created_at")