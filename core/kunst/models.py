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
    titel = models.CharField(max_length = 200, default = 'geen')
    
    def __str__(self):
        return f" -- {self.created_by}"
### //TENTOONSTELLING

## TELLER - AANTAL BEZOEKERS ##
class VisitorDashboard(models.Model):
    class Meta:
        managed = False # geen tabel in DB ivm nep model 
        verbose_name = "Bezoekers Dashboard"
        verbose_name_plural = "Bezoekers Dashboard"
        app_label = "kunst"   # <-- zet hier de naam van jouw app
## TELLER - AANTAL BEZOEKERS ##

## TELLER - AANTAL BEZOEKERS  OPTIE NIET GEBRUIKT##
class Visitor(models.Model):
  ip_address = models.GenericIPAddressField() # ip adress van de bezoeker
  page = models.CharField(max_length = 50, blank=False) # pagina die bezocht is
  timestamp= models.DateTimeField(default = timezone.now) # tijdstip van bezoek
  user_agent = models.CharField(max_length = 255, null = True, blank=True) #Browser info
  
  def __str__(self):
    return f"{self.ip_address} bezocht {self.page} om {self.timestamp}"
## // TELLER - AANTAL BEZOEKERS ##