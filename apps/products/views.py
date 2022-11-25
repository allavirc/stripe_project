from typing import Any

import stripe
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.http import JsonResponse
from products.models import Item
from settings import base


stripe.api_key = base.STRIP_SECRET_KEY


class SuccessPageView(TemplateView):
    template_name = 'success.html'


class CancelPageView(TemplateView):
    template_name = 'cancel.html'


class ProductPageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(
            ProductPageView,
            self
        ).get_context_data(**kwargs)
        context.update({
            "STRIPE_PUBLIC_KEY": base.STRIP_SECRET_KEY
        })
        return context




# def product(request):
#     all_products = Item.objects.all()
#     return render(
#         request,
#         'home.html',
#         context={
#             'products': all_products,
#
#         }
#     )


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        product_id = self.kwargs["pk"]
        product = Item.objects.get(id=product_id)
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': product.price,
                        'product_data': {
                            'name': product.name,
                            # 'images': ['https://i.imgur.com/EHyR2nP.png'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                "product_id": product.id
            },
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })
