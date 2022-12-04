from django.urls import path
from .endpoint import view, auth_views

urlpatterns = [
    path('', auth_views.google_login)
]
