from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import C_Details, Bill_Record

# Create your views here.

class IndexView(generic.ListView):
    template_name = "accounting/index.html"
    context_object_name = 'latest_CustID'

    def get_queryset(self):
        return C_Details.objects.order_by('-PendingAmount')[:5]

"""
def index(request):
    latest_CustID = C_Details.objects.order_by('-PendingAmount')[:5]
    context = { 'latest_CustID' : latest_CustID }
    return render(request, 'accounting/index.html', context)

class DetailView(generic.DetailView):
    model = C_Details
    template_name = 'accounting/detail.html'
"""

def detail(request, CustID):
    cust_id = get_object_or_404(C_Details, pk=CustID)
    return render(request, 'accounting/detail.html', {'cust_id' : cust_id})


def newBill(request):
    cust_id = C_Details.objects.all()
    return render(request, 'accounting/newBill.html', {'cust_id' : cust_id})

def save_bill(request):
    cust_id = get_object_or_404(C_Details, pk=request.POST['customer_info'])
    try:
        inp = cust_id.bill_record_set.create(Date=request.POST['date'], Amount=request.POST['Amount'])
    except (KeyError, Bill_Record.DoesNotExist):
        return render(request, 'accounting/detail.html', {
            'error_message' : "Some error is there",
        })
    else:
         inp.save()
         return HttpResponseRedirect(reverse('accounting:detail', args=(cust_id.CustID,)))

def newPayment(request):
    cust_id = C_Details.objects.all()
    return render(request, 'accounting/newPayment.html', {'cust_id' : cust_id})

def save_payment(request):
    cust_inf = get_object_or_404(C_Details, pk=request.POST['customer_info'])
    try:
        inp = cust_inf.payment_record_set.create(Date=request.POST['date'], Amount=request.POST['Amount'])
    except (KeyError, Payment_Record.DoesNotExist):
        return render(request, 'accounting/detail.html', {
            'error_message' : "Some error in payment",
        })
    else:
        inp.save()
        return HttpResponseRedirect(reverse('accounting:detail', args=(cust_inf.CustID,)))

def paymentPage(request, CustID):
    response = "This is the payment page of  %s"
    return HttpResponse(response % CustID)
