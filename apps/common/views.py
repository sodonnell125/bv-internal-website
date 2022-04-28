from re import template
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
from django.views.generic import TemplateView

class LandingView(TemplateView):
    template_name = 'common/home.html'

class LoginView(TemplateView):
    template_name = 'common/hom.html'

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'common/dashboard.html'
    login_url = reverse_lazy('home')

