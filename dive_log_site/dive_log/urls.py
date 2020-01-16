from django.urls import path
from .views import DiveListView, DiveDetailView

urlpatterns = [
    path('dive/<int:pk>/', DiveDetailView.as_view(), name='dive_details'),
    path('', DiveListView.as_view(), name='home'),
]