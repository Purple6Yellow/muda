from django.shortcuts import render, get_object_or_404
from .models import Kunst, Decor, Werk, Tent
from django.views.generic import ListView, DetailView

### -- INDEX-- ### 
def index(request):
  kunst = Kunst.objects.latest('created_by')
  werk = Werk.objects.latest('created_by')
  decor = Decor.objects.latest('created_by')
  tent = Tent.objects.latest('created_by')
  return render(request, 'index.html', {'kunst': kunst, 'werk': werk, 'decor': decor, 'tent': tent})
### // INDEX-- ###
#  
### -- ALGEMEEN -- ### 
def cv(request):
    return render (request, 'cv.html' )
def contact(request):
    return render (request, 'contact.html' )
### // ALGEMEEN -- ### 


### -- DECORATIE -- ### 
def decor (request):
    print('request decor')
    #decors = Decor.objects.order_by('created_by').reverse
    decors= Decor.objects.all()
    print(decors)
    print (Decor.objects.all())
    return render(request,'decoratie.html', {'decors': decors})
### // DECORATIE -- ### 

### -- AANHETWERK -- ### 
class OverzichtWerk(ListView):
    model = Werk

class DetailWerk(DetailView):
    model = Werk
    template_name = 'werk_detail.html'
    
def werk (request):
    print('request werk')
    #decors = Decor.objects.order_by('created_by').reverse
    werks= Werk.objects.order_by('created_by').reverse
    print ("werk:", Werk.objects.all())
    return render(request,'aanhetwerk.html', {'werks': werks})
### // AANHETWERK -- ### 

### -- KUNST -- ### 
class OverzichtKunst(ListView):
    model = Kunst

class DetailKunst(DetailView):
    model = Kunst
    template_name = 'kunst_detail.html'

def kunst(request):
   # kunsts = Kunst.objects.all()
    # kunsts = Kunst.objects.order_by('created_by').reverse
    kunsts = Kunst.objects.order_by('-created_by')
    print(kunsts)
    return render(request,'kunst.html', {'kunsts': kunsts})
### // KUNST -- ### 


### -- DECOR -- ### 
class OverzichtDecor(ListView):
    model = Decor

class DetailDecor(DetailView):
    model = Decor
    template_name = 'decoratie_detail.html'

def decor(request):
   # kunsts = Kunst.objects.all()
    # kunsts = Kunst.objects.order_by('created_by').reverse
    decors = Decor.objects.order_by('-created_by')
    return render(request,'decoratie.html', {'decors': decors})
### // DECOR -- ### 

 










