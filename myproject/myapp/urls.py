from django.urls import path
from .views import people_list

urlpatterns = [
    path('', people_list, name='people_list'),
]
