from django.shortcuts import render, get_object_or_404, redirect
from .forms import PaymentForm
from django.conf import settings
from django.contrib import messages
from .models import Payment

# Create your views here.
def start_payment(request):
    if request.method == "POST":
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
            return render(request, 'flutterwave/make_payment.html', {'payment': payment,
                                                                     'flutter_public_key': settings.FLUTTERWAVE_PUBLIC_KEY})
    else:
        payment_form = PaymentForm()
        return render(request, 'flutterwave/initiate_payment.html', {'payment_form': payment_form})

def payment_verification(request, id: str):
    payment = get_object_or_404(Payment, id=id)
    verified = payment.payment_verification()
    if verified:
        messages.success(request, 'Verification Successful')
    else:
        messages.error(request, 'Verification Failed')
    return redirect('start_payment')
