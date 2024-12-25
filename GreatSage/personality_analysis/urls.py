from django.urls import path
from personality_analysis import views
urlpatterns = [
    path("landing/", views.landing, name="landing"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("textAnalysis/", views.text, name="text"),
    path('result/', views.result, name='result'),
    path('handwritingAnalysis', views.handwriting, name="handwriting"),
    path('conversation', views.conversation, name= 'conversation')
]