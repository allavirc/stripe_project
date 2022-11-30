import json
import stripe

# Django
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.views import View

# Apps
from products.models import Item
from settings import base


stripe.api_key = base.STRIPE_SECRET_KEY


class HomePageView(TemplateView):
    template_name = "home.html"

def product(request):
    all_products = Item.objects.all()
    return render(
        request,
        'home.html',
        context={
            'products': all_products,

        }
    )

class SuccessPageView(TemplateView):
    template_name = "success.html"


class CancelPageView(TemplateView):
    template_name = "cancel.html"


class ProductBuyPageView(TemplateView):
    template_name = "buying.html"


    def get_context_data(self, id, **kwargs):
        try:
            print(id)
            product = Item.objects.get(id=id)

        except Exception as e:
            print(e)
        context = super(ProductBuyPageView, self).get_context_data(**kwargs)
        context.update({
            "product": product,
            "STRIPE_PUBLIC_KEY": base.STRIPE_PUBLIC_KEY
        })
        return context


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


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, base.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Некорректный платеж
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Некорректная подпись
        return HttpResponse(status=400)


    # Обработка события checkout.session.completed
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        customer_email = session["customer_details"]["email"]
        product_id = session["metadata"]["product_id"]

        product = Item.objects.get(id=product_id)

        send_mail(
            subject="Here is your product",
            message=f"Thanks for your purchase. Here is the product you ordered. The URL is {product.url}",
            recipient_list=[customer_email],
            from_email="matt@test.com"
        )

        # TODO - при отправке ссылки на продукт
    
    elif event["type"] == "payment_intent.succeeded":
        intent = event['data']['object']

        stripe_customer_id = intent["customer"]
        stripe_customer = stripe.Customer.retrieve(stripe_customer_id)

        customer_email = stripe_customer['email']
        product_id = intent["metadata"]["product_id"]

        product = Item.objects.get(id=product_id)

        send_mail(
            subject="Hello! You bought this perfume in our store!",
            message=f"Thanks for your purchase. Here is the product you ordered. The name is {product.name}",
            recipient_list=[customer_email],
            from_email="allavirc2@gmail.com"
        )

    return HttpResponse(status=200)


class StripeIntentView(View):
    def post(self, request, id, *args, **kwargs):
        try:
            req_json = json.loads(request.body)
            customer = stripe.Customer.create(email=req_json['email'])
            product = Item.objects.get(id=id)
            intent = stripe.PaymentIntent.create(
                amount=product.price,
                currency='usd',
                customer=customer['id'],
                metadata={
                    "product_id": product.id
                }
            )
            return JsonResponse({
                'clientSecret': intent['client_secret']
            })
        except Exception as e:
            return JsonResponse({'error': str(e)})
