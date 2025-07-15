from django.urls import path
from .views import DetailKunst, DetailDecor,DetailWerk, cv, kunst, decor, werk, contact, index
# from .views import index, decor
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [

### -- ALGEMEEN -- ### 
    path('cv.html/', cv),
    path('contact.html/',contact),
### // ALGEMEEN -- ### 
### -- DECORATIE -- ### 
    path('decoratie.html/', decor, name = 'decor'),
    path('decoratie_detail.html/<int:pk>/', DetailDecor.as_view(), name = 'DecorDetail'),
### // DECORATIE -- ### 
### -- KUNST -- ### WERKT NOG NIET
    path('kunst.html/', kunst, name = 'kunst'),
    path('kunst_detail.html/<int:pk>/', DetailKunst.as_view(), name = 'KunstDetail'),
### // KUNST -- ### 
### -- WERK -- ### 
    path('aanhetwerk.html/', werk, name = 'werk' ),
    path('aanhetwerk_detail.html/<int:pk>/', DetailWerk.as_view(), name = 'WerkDetail'),
### // WERK -- ### 
######---INDEX----############
    path('index.html/', index),
 
 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


