from django.shortcuts import render
from .models import Menu, Order, Customer
# Create your views here.
from django.views.generic import ListView, DetailView


class IndexView(ListView):
    model = Menu


class DetailView(DetailView):
    model = Menu


