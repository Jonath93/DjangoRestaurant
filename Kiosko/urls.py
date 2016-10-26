from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^$', views.ProductKiosko.as_view(), name='product')
]