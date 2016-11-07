from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^$', views.ProductKiosko.as_view(), name='product'),
    #/productComida
    url(r'^(?P<category_id>[0-9]+)/$', views.ProductComida, name='productComida'),

    url(r'^order/$', views.OrderCreate.as_view(), name='order')
    
]