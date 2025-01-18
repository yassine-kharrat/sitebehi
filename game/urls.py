from django.urls import path
from .views import ScenarioView, FeedbackView

urlpatterns = [
    path('scenarios/', ScenarioView.as_view(), name='scenarios'),
    path('scenarios/feedback/', FeedbackView.as_view(), name='feedback'),
]
