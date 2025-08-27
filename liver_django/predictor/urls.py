from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),       # Home page
    path("predict/", views.predict_page, name="predict_page"),  # Prediction form & result
    
]
