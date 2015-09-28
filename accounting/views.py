from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from .models import C_Details

# Create your views here.

def index(request):
    latest_CustID = C_Details.objects.order_by('-PendingAmount')[:5]
    context = { 'latest_CustID' : latest_CustID }
    return render(request, 'accounting/index.html', context)

def detail(request, CustID):
    cust_id = get_object_or_404(C_Details, pk=CustID)
    return render(request, 'accounting/detail.html', {'cust_id' : cust_id})

def paymentPage(request, CustID):
    response = "This is the payment page of  %s"
    return HttpResponse(response % CustID)
