from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<CustID>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<CustID>[0-9]+)/paymentPage/$', views.paymentPage, name='paymentPage')
]
