from django.db import models
from PIL import Image
from django.utils import timezone

### KUNST
class Kunst(models.Model):
    titel = models.CharField(max_length=200)
    afbeeld = models.ImageField(upload_to='images/', null = True, blank = True)
    jaartal = models.IntegerField(default ="2025", null = True)
    materiaal = models.CharField(max_length=200, default = "algemeen", null = True)
    formaat = models.CharField(max_length=200,  default = "algemeen")
    created_by = models.DateTimeField(default=timezone.now)
    pass
### //KUNST

### DECOR
class Decor (models.Model):
    titel = models.CharField(max_length=200)
    afbeeld = models.ImageField(upload_to='images/', null = True, blank = True)
    jaartal = models.IntegerField(default ="2025", null = True)
    materiaal = models.CharField(max_length=200, default = "algemeen", null = True)
    formaat = models.CharField(max_length=200,  default = "algemeen")
    created_by = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.titel} -- {self.created_by}"
### //DECOR

### WERK
class Werk (models.Model):
    titel = models.CharField(max_length=200)
    afbeeld = models.ImageField(upload_to='images/', null = True, blank = True)
    created_by = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.titel} -- {self.created_by}"
### //WERK

### TENTOONSTELLING
class Tent(models.Model):
    afbeeld = models.ImageField(upload_to='images/', null = True, blank = True)
    created_by = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f" -- {self.created_by}"
### //TENTOONSTELLING