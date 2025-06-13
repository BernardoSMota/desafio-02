from django.db import models

# Create your models here.
class Funcionario(models.Model):
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    city = models.CharField(max_length=32)
    
    def __str__(self):
        return self.name