from django.shortcuts import render,get_object_or_404,render_to_response
from django.http import Http404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.template import loader,RequestContext
from django.views import generic
from .models import SaleOrder,ProductTemplate

# Create your views here.
def Index(request):
    return render_to_response('home/index.html')

class ProductKiosko(generic.ListView):
    model = ProductTemplate
    context_object_name='latest_name_list'
    template_name = 'kiosko.html'


