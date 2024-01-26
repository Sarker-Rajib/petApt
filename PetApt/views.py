from django.shortcuts import render
from Pets import models

def home(request, category_slug=None):
    pets = models.Pet.objects.all()
    category = models.PetCategory.objects.all()

    if category_slug is not None:
        filterOption = models.PetCategory.objects.get(slug = category_slug)
        pets = models.Pet.objects.filter(category = filterOption)
    return render(request, 'index.html', {'pets': pets, 'category': category})