from django.urls import path
from .views import DetailKunst, KunstTemplate1, KunstTemplate2, cv, kunst, decor, werk, contact
# from .views import index, decor
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [

### -- ALGEMEEN -- ### 
    path('cv.html/', cv),
    path('contact.html/',contact),
### // ALGEMEEN -- ### 
### -- DECORATIE -- ### 
    path('decoratie.html/', decor),
### // DECORATIE -- ### 
### -- KUNST -- ### WERKT NOG NIET
    path('kunst.html/', kunst),
    path('kunst_detail.html/<int:pk>/', DetailKunst.as_view(), name = 'KunstDetail'),
### // KUNST -- ### 
### -- WERK -- ### 
    path('aanhetwerk.html/', werk),
### // WERK -- ### 

### -- KUNST -- ### WERKT NOG NIET
    path('kunst.html/', KunstTemplate1.as_view(), name = 'Kunst'),
    path('index.html/', KunstTemplate2.as_view(), name = 'index'),
    #path('aanhetwerk.html/', KunstTemplate3.as_view(), name = 'Werk'),
### // KUNST -- ### 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
