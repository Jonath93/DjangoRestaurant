from django.shortcuts import render,get_object_or_404,render_to_response
from django.http import Http404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.template import loader,RequestContext
from django.views import generic
from .models import SaleOrder,ProductTemplate,PosCategory,SaleOrderLine
from .forms import SaleOrderLineForm,SaleOrderForm

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
        categoria=PosCategory.objects.all()
    except ProductTemplate.DoesNotExist:
        raise Http404("No existe esa categoria")
    return render(request,'btn/btncomida.html',{'category':product_list,'latest_name_list':categoria})

class OrderCreate(generic.CreateView):
    model=SaleOrderLine
    template_name='btn/formulario_orden.html'
    form_class = SaleOrderLineForm
    success_url=reverse_lazy('home/index.html')
    
    def get_context_data(self, **kwargs):
        context = super(OrderCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self,request,*args,**kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            SaleOrderLine.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form,form2=form))