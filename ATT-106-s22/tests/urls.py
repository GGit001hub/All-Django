from django.urls import path
from .views import QuestionsViewAPI

urlpatterns = [
    path('',QuestionsViewAPI.as_view()),
]
