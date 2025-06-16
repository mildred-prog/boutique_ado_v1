from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm
import logging

logger = logging.getLogger(__name__)

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    
    # Add debug logging
    stripe_public_key = 'pk_test_51RadTXJy3jGoDeqvDwnOuf55mGRb0T1aBOOhTKlIJ3kdcBIj7PZM39QI0fVxEgGtqtyGalIASVKuqjyoyT3tWft400EOwcxfCw'
    client_secret = 'test_client'
    
    logger.debug(f"Stripe public key: {stripe_public_key}")
    logger.debug(f"Client secret: {client_secret}")
    
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': client_secret,
    }

    return render(request, template, context)
