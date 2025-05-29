from django.urls import path
from .views import OverzichtKunst, DetailKunst, menu, deco_vie, KunstTemplate1, KunstTemplate2,  KunstTemplate3, Decoratie, cv, product_list, kunst
# from .views import index, decor
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
   # path('kunst_overzicht.html/', OverzichtKunst.as_view(), name = 'KunstOverzicht'),
    path('kunst_detail.html/<int:pk>/', DetailKunst.as_view(), name = 'KunstDetail'),
    path('menu.html/', menu),
    path('cv.html/', cv),
    #path('aanhetwerk.html/', product_list),
    path('kunst.html/', kunst),
    path('decoratie.html/', deco_vie),
    #path('index.html/', index),
    #path('decoratie.html/', decor),

    ###
    path('kunst.html/', KunstTemplate1.as_view(), name = 'Kunst'),
    path('index.html/', KunstTemplate2.as_view(), name = 'index'),
    #path('decoratie.html/', Decoratie.as_view(), name = 'Decor'),
    path('aanhetwerk.html/', KunstTemplate3.as_view(), name = 'Werk'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)