from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^$', views.CategoryKiosko.as_view(), name='Category'),
    #/productComida
    url(r'^(?P<category_id>[0-9]+)/$', views.ProductComida, name='productComida'),

    url(r'^order/$', views.OrderCreate, name='order')
    
]