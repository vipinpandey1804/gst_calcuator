from django.urls import path
from gst import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
]