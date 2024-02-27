from django.db import models

# Create your models here.

class customDesign(models.Model):

    name = models.CharField(max_length=200)
    email = models.EmailField()
    design = models.TextField()

    def __str__(self):
        return self.name
    
class contactForm(models.Model):

    name = models.CharField(max_length=200)
    email = models.EmailField()
    descp = models.TextField()

    def __str__(self):
        return self.name