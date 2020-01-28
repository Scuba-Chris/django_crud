from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Dive
from django.urls import reverse_lazy

class DiveListView(ListView):
    model = Dive
    template_name = 'home.html'

class DiveDetailView(DetailView):
    model = Dive
    template_name = 'dive_details.html'

class DiveCreateView(CreateView):
    model = Dive
    template_name = 'new_dive.html'
    fields = ['title', 'author', 'body']

class DiveUpdateView(UpdateView):
    model = Dive
    template_name = 'dive_update.html'
    fields = ['title', 'body']

class DiveDeleteView(DeleteView):
    model = Dive
    template_name = 'dive_delete.html'
    success_url = reverse_lazy('home')
