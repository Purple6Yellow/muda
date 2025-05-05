from django.shortcuts import render
from .models import Kunst
from django.views.generic import ListView, DetailView


### Kunst
class OverzichtKunst(ListView):
    model = Kunst

    
class KunstTemplate2(OverzichtKunst):
    def get_queryset(self):
        context = Kunst.objects.order_by('created_by')[7:8]
        #print(context)
        return context
    
    template_name = 'index.html'
    #print('index.html')

class KunstTemplate1(OverzichtKunst):
    def get_queryset(self):
        context = Kunst.objects.all()
        #print(context)
        return context

    template_name = 'kunst.html'
    print("kunst.html")

class KunstTemplate3(OverzichtKunst):
    template_name = 'decoratie.html'
    print("decor.html")


class DetailKunst(DetailView):
    model = Kunst
    template_name = 'kunst_detail.html'

###// Kunst

def kunst(request):
   # kunsts = Kunst.objects.all()
    kunsts = Kunst.objects.order_by('created_by').reverse
    return render(request,'kunst.html', {'kunsts': kunsts})

def deco(request):
    decos = Kunst.objects.all()
    return render(request,'decoratie.html', {'decos': decos})


def product_list(request):
    products = Kunst.objects.all()
    return render (request, 'aanhetwerk.html', {'products': products})


###ALGEMEEN
def index(request):
  return render (request, 'index.html' )
def menu(request):
    return render (request, 'menu.html' )
def cv(request):
    return render (request, 'cv.html' )

#def decor(request):
#    return render (request, 'decoratie.html' )

###//ALGEMEEN