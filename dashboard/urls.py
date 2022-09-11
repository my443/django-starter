from django.urls import path

from . import views
from .views import Update

urlpatterns = [
    path('', views.hello, name='hello'),
    path('row/<slug:pk>/', Update.as_view(), name='row_update'),
]