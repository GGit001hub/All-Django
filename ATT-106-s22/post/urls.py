from django.urls import path
from .views import TeacheCreateViewAPI,StudentCreateViewAPI


urlpatterns = [
    path('teacher/',TeacheCreateViewAPI.as_view()),
    path('student/',StudentCreateViewAPI.as_view()),
]
