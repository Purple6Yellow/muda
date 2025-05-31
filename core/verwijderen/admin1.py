from django.contrib import admin
from ..kunst.models import Kunst, Decor, Werk

admin.site.site_header = "Admin omgeving Marlous Muda Art"


#admin.site.register(Kunst)
@admin.register(Kunst)
class KunstAdmin(admin.ModelAdmin):
    list_display = ( "titel","created_by")
    list_filter = ("titel",)
    pass

#admin.site.register(Decor)
@admin.register (Decor)
class DecorAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter("titel")
    
#admin.site.register(Werk)
@admin.register (Werk)
class WerkAdmin(admin.ModelAdmin):
    list_display = ( "titel","created_by")
    list_filter = ("titel",)
    pass