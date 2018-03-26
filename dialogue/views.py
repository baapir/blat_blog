from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models

# Create your views here.
class BlatListView(ListView):
    model = models.Blta

class BlatDetailView(DetailView):
    model = models.Blat
