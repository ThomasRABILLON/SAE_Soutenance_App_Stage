from django.shortcuts import render

from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse_lazy
from django.views.generic import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.forms.models import BaseModelForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "app_etudiant/etudiant_home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['titreh1'] = "Hello "

    def post(self, request, **kwargs):
        return render(request, self.template_name)
    
