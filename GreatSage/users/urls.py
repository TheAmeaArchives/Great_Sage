from django.urls import path
from .views import logins,logouts, signup, index

urlpatterns=[
    path('', index, name='index'),
    path('logins/', logins, name="logins"),
    path('logouts/', logouts, name="logouts"), # type: ignore
    path("signup/", signup, name= "signup"),
]