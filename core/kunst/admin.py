from django.contrib import admin
from .models import Kunst, Decor, Werk, Tent

admin.site.site_header = "Admin omgeving Marlous Muda Art"

###KUNST###
#admin.site.register(Kunst)
@admin.register(Kunst)
class KunstAdmin(admin.ModelAdmin):
    list_display = ( "titel","created_by", )
    list_filter = ("titel",)
    pass
###KUNST###

###DECOR###
@admin.register(Decor)
class DecorAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter("titel")
###DECOR###

###WERK###
@admin.register(Werk)
class WerkAdmin(admin.ModelAdmin):
    list_display = ( "titel","created_by",)
    list_filter = ("titel",)
    pass
###WERK###

