from django.contrib import admin

# Register your models here.
from .models import PetCategory, Pet, Review

# Register your models here.
class BrandSlug(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
    list_display = ['name', 'slug']

admin.site.register(PetCategory, BrandSlug)
admin.site.register(Pet)
admin.site.register(Review)