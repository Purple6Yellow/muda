
###BEZOEKERS_TELLER###
class MijnAdminSite(admin.AdminSite):
    site_header = "Mijn Admin"

    def get_urls(self):
        urls = super().get_urls() #   Haal de standaard admin Urls
        extra_urls = [
            path('mijn-pagina/', self.admin_view(self.mijn_custom_pagina), name = 'mijn-pagina')
        ]
        return extra_urls + urls #Voeg je custom URL toe
    
    def mijn_custom_pagina(self, request):
        #context voor je template
        context = dict(
            self.each_context(request), # belangrijk admin context
            titel = 'Welkom op mijn custom pagina'

        )
        return render(request, "admin/mijn_custom_template.html", context)
    
###BEZOEKERS_TELLER###
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
    
admin.site.register(VisitorDashboard, VisitorDashboardAdmin)
###BEZOEKERS_TELLER###


###BEZOEKERS_TELLER###WERK NIET
class VisitorAdminSite(admin.AdminSite):
    site_header = "Mijn Admin"

    def get_urls(self):
        urls = super().get_urls()
        extra_urls =[
            path("dashboard/", self.admin_view(self.dashboard_view), name="visitor-dashboard"),
        ]
        return extra_urls + urls 
    
    def dashboard_view(self, request):
        stats = { 
            "today": 123,
            "this_week": 842,
            "this_month": 3102,
        }
        context = dict (
            self.each_context(request),
            stats = stats,
            title = "Bezoekers Dashboard",
        )
        return TemplateResponse(request, "admin/visitor_dashboard.html", context)
    
custom_admin_site = VisitorAdminSite (name = "custom_admin")


###BEZOEKERS_TELLER###



urls.py werkblad:
from .admin import MijnAdminSite #bezoeker-teller

admin_site = MijnAdminSite(name = 'mijn_admin')

###BEZOEKERS_TELLER###
   
    path('admin/', admin_site.urls),


###DECOR###
@admin.register(Decor)
class DecorAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter("titel")
###DECOR###