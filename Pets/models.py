from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.

class PetCategory(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=80)

    def __str__(self):
        return self.name
    
class Pet(models.Model):
    image = models.ImageField(upload_to='pets/media/images/')
    title = models.CharField(max_length = 40)
    description = models.TextField()
    adapt_price = models.IntegerField()
    category = models.ForeignKey(PetCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Review(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='feedbacks')
    name = models.CharField(max_length=20, blank=True)
    body = models.TextField(verbose_name='Your Feedback')
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Feedback by {self.name}"