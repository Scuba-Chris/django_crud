from django.urls import path
from .views import DiveListView, DiveDetailView, DiveCreateView, DiveUpdateView, DiveDeleteView

urlpatterns = [
    path('dive/<int:pk>/', DiveDetailView.as_view(), name='dive_details'),
    path('', DiveListView.as_view(), name='home'),
    path('dive/new/', DiveCreateView.as_view(), name='new_dive'),
    path('dive/<int:pk>/edit', DiveUpdateView.as_view(), name='dive_update'),
    path('dive/<int:pk>/delete', DiveDeleteView.as_view(), name='dive_delete')

]