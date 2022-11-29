from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from settings import base
from apps.products.views import (
    CreateCheckoutSessionView,
    ProductBuyPageView,
    SuccessView,
    CancelView,
    stripe_webhook,
    StripeIntentView,
    HomePageView,
    product
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-payment-intent/<int:id>/', StripeIntentView.as_view(), name='create-payment-intent'),
    path('webhooks/stripe/', stripe_webhook, name='stripe-webhook'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('', product, name='home'),
    path('', HomePageView.as_view(), name='home'),
    path('buy/<int:id>', ProductBuyPageView.as_view(), name='buying-page'),
    path('create-checkout-session/<int:id>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session')
] + static(
    base.MEDIA_URL,
    document_root=base.MEDIA_ROOT
)
