from django.urls import path
from .views import PetDetails

urlpatterns = [
    path('pet-details/<int:id>', PetDetails.as_view(), name='petDetails')
]