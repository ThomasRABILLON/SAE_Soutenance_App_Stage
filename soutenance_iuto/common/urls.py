from django.urls import path

from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.BaseView.as_view(), name='base_common'),
]
