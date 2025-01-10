from django.urls import path

from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.BaseView.as_view(), name='home_common'),
    path('home', views.BaseView.as_view(), name='home_common'),
    path('login/', views.LoginView.as_view(), name='login_common'),
]
