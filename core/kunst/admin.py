from django.contrib import admin
from .models import Kunst

admin.site.site_header = "Admin omgeving Marie Louise Art"


#admin.site.register(Kunst)
@admin.register(Kunst)
class KunstAdmin(admin.ModelAdmin):
    list_display = ( "titel","created_by")
    list_filter = ("titel",)
    pass
