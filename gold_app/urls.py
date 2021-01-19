from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('place/<str:place>', views.process_money),
    path('win_conditions', views.win),
    path('reset', views.reset),
]