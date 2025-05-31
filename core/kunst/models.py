from django.db import models
from PIL import Image
from django.utils import timezone

### Kunst
class Kunst (models.Model):
    titel = models.CharField(max_length=200)
    afbeeld = models.ImageField(upload_to='images/', null = True, blank = True)
    afbeeld_name = models.CharField(max_length = 100, blank=True)
    created_by = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.titel} -- {self.created_by}"
### //Kunst

### DECOR
class Decor (models.Model):
    titel = models.CharField(max_length=200)
    afbeeld = models.ImageField(upload_to='images/', null = True, blank = True)
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