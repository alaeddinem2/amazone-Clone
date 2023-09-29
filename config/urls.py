from django.urls import path
from .views import home
app_name = 'config'

urlpatterns = [
    path('', home),
   
]