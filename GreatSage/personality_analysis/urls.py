from django.urls import path
from personality_analysis import views
urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("textAnalysis/", views.text, name="text"),
    path('result/', views.result, name='result'),
    # path('handwritingAnalysis', views.handwriting, name="sound_analysis"),
    path('conversation', views.conversation, name= 'conversation'),
    # path('soundtrack/', views.sound_analysis, name= 'soundtrack'),
]