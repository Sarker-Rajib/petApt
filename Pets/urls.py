from django.urls import path
from .views import PetDetails, add_pet

urlpatterns = [
    path('add-pet/', add_pet, name='add_pet'),
    path('pet-details/<int:id>', PetDetails.as_view(), name='petDetails')
]