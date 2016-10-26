from django.shortcuts import render,get_object_or_404,render_to_response
from django.http import Http404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.template import loader,RequestContext
from django.views import generic
from .models import SaleOrder,ProductTemplate,PosCategory
# Create your views here.
def Index(request):
    return render_to_response('home/index.html')

class ProductKiosko(generic.ListView):
    model = PosCategory
    context_object_name='latest_name_list'
    template_name='view/kiosko.html'


def ProductComida(request,category_id):
    try:
        product_list=ProductTemplate.objects.filter(pos_categ_id=category_id)
    except ProductTemplate.DoesNotExist:
        raise Http404("No existe esa categoria")
    return render(request,'btn/btncomida.html',{'category':product_list})
    