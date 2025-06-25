from django.shortcuts import render, get_object_or_404
from .models import Kunst, Decor, Werk
from django.views.generic import ListView, DetailView

### -- INDEX-- ### 
def index(request):
  kunst = Kunst.objects.latest('created_by')
  werk = Werk.objects.latest('created_by')
  decor = Decor.objects.latest('created_by')
  return render(request, 'index.html', {'kunst': kunst, 'werk': werk, 'decor': decor})
### // INDEX-- ### 
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


### -- KUNSTDETAIL-- ### 
def kunst_detail(request):
  kunst = Kunst.objects.all
  return render(request, 'kunst_detail.html', {'kunst': kunst})
### // KUNSTDETAIL- ### 

### -- DECORDETAIL-- ### 
def decor_detail(request):
  kunst = Decor.objects.all
  return render(request, 'decoratie_detail.html', {'decor': decor})
### // DECORDETAIL- ### 



##### UITPROBEREN 
def KunstPK(request,pk):
    item = get_object_or_404(Kunst,pk=pk )
    try:
        next_item = Kunst.objects.filter(pk__gt=pk).order_by('pk').first()
    except Kunst.DoesNotExist:
        next_item = None
    context ={
        'item':item,
        'next_item':next_item, 
    }
    print(next_item)
    return render(request, 'kunst_detail.html', context)
##### UITPROBEREN 

##### UITPROBEREN 2


######### NODIG OM MODELS OP MEERDERE VERSCHILLENDE PAGINA'S TE SHOWEN 
class KunstTemplate1(OverzichtKunst):
    print('KunstTemplate1')
    def get_queryset(self):
        context = Kunst.objects.all()
        #print(context)
        return context

    template_name = 'kunst.html'
    print("kunst.html")

class KunstTemplate2(OverzichtKunst):
    print('KunstTemplate2')
    def get_queryset(self):
        context = Kunst.objects.latest('created_by')
        #print(context)
        return context
    
    template_name = 'index.html'
    #print('index.html')

class KunstTemplate3(OverzichtKunst):
    print('KunstTemplate3')
    def get_queryset(self):
        context = Kunst.objects.order_by('created_by')[7:8]
        #print(context)
        return context
    
    template_name = 'basis.html'
    #print('index.html')
### // KUNST -- ### 





### VERWIJDJEREN ###






def werk3(request):
    werk = Kunst.objects.all()
    return render(request,'basis.html', {'werk': werk})


def product_list(request):
    products = Kunst.objects.all()
    return render (request, 'basis.html', {'products': products})


###ALGEMEEN


#def decor(request):
#    return render (request, 'decoratie.html' )

###//ALGEMEEN

### VERWIJDJEREN ###