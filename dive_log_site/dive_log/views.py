from django.views.generic import ListView, DetailView,DeleteView, UpdateView
from .models import Dive

class DiveListView(ListView):
    model = Dive
    template_name = 'home.html'

class DiveDetailView(DetailView):
    model = Dive
    template_name = 'dive_details.html'