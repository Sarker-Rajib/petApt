from django.db import models
from django.contrib.auth.models import User
from Pets.models import Pet

# Create your models here.
class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='depositAccount')
    account_no = models.IntegerField(unique=True)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.account_no}'

class AdaptPet(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    adaptedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp= models.DateTimeField()
    
    class Meta:
        ordering = ['timestamp']
    
    def __str__(self) -> str:
        return f'{self.pet.title}'