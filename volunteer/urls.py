from django.urls import path
from . import views

urlpatterns = [
    path('', views.volunteer_form, name='volunteer_form'),
    path('thank-you/', views.thank_you_page, name='thank_you_page'),
    path('export-csv/', views.export_volunteers_to_csv, name='export_volunteers_to_csv'),
]
