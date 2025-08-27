# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     # path('api/predict/', views.api_predict, name='api_predict'),
#     path('predict/', views.predict_page, name='predict_page'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),       # Home page
    path("predict/", views.predict_page, name="predict_page"),  # Prediction form & result
    
]
