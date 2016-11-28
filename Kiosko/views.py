from django.shortcuts import render, render_to_response
from django.http import Http404
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import csrf_protect
from django.views import generic
from django.forms.formsets import formset_factory, BaseFormSet
from .models import *
from .forms import *


# Create your views here.
def Index(request):
    return render_to_response('home/index.html')


class CategoryKiosko(generic.ListView):
    model = PosCategory
    context_object_name = 'latest_name_list'
    template_name = 'view/kiosko.html'

def ProductComida(request, category_id):
    try:
        product_list = ProductTemplate.objects.filter(pos_categ_id=category_id)
        categoria = PosCategory.objects.all()
    except ProductTemplate.DoesNotExist:
        raise Http404("No existe esa categoria")
    return render(request, 'pages/btncomida.html', {'product_list': product_list, 'latest_name_list': categoria})


def OrderCreate(request):
    class RequiredFormSet(BaseFormSet):
        def __init__(self, *args, **kwargs):
            super(RequiredFormSet, self).__init__(*args, **kwargs)
            for form in self.forms:
                form.empty_permitted = False

    SaleOrderLineFormSet = formset_factory(SaleOrderLineForm, formset=RequiredFormSet,max_num=10)
    idobject = SaleOrder.objects.latest('id')
    sumaid = 'SO' + str(idobject.id + 1)

    if request.method == 'POST':
        form2 = SaleOrderForm(request.POST or None, initial={'name': sumaid})
        #form3 = SaleOrderTaxForm(request.POST)
        formset = SaleOrderLineFormSet(request.POST)
        if form2.is_valid() and formset.is_valid():
            saleorder = form2.save()

            for forms in formset:
                saleorderline = forms.save(commit=False)
                saleorderline.order_id = saleorder.id
                saleorderline.save()
                #form3.order_line_id = saleorderline.id
                #form3.save()
            return HttpResponseRedirect('/')
    else:
        form2 = SaleOrderForm(initial={'name': sumaid})
        formset = SaleOrderLineFormSet()



    return render(request, 'pages/formulario_orden.html', {'form': form2, 'formset': formset})


