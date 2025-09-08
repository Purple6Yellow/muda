from django.db import models
from PIL import Image
from django.utils import timezone

### Kunst
class Kunst (models.Model):
    titel = models.CharField(max_length=200)
    afbeeld = models.ImageField(upload_to='images/', null = True, blank = True)
    jaartal = models.IntegerField(default =None)
    materiaal = models.CharField(max_length=200, default = None)
    formaat = models.CharField(max_length=200,  default = None)
    created_by = models.DateTimeField(default=timezone.now)
    oude_Naam= models.CharField(max_length=200, default = None)

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



######################
admin.py

class VisitorDashboardAdmin(admin.ModelAdmin):
    change_list_template = "admin/visitor_dashboard.html"

    def changelist_view(self, request, extra_context=None):
    # Hier kun je je eigen logica doen, bv. data uit de database halen
        stats = {
            "today": 123,
            "this_week": 842,
            "this_month": 3102,
        }
        context = {"stats": stats}
        return TemplateResponse(request, "admin/visitor_dashboard.html", context)
    
class VisitorDashboard(models.Model):
    class Meta:
        managed = False  # geen tabel in DB ivm nep model 
        verbose_name = "Bezoekers Dashboard"
        verbose_name_plural = "Bezoekers Dashboard"
        app_label = "kunst"   # <-- zet hier de naam van jouw app

admin.site.register(VisitorDashboard, VisitorDashboardAdmin)