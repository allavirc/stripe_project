from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from products.views import (
    CreateCheckoutSessionView,
    ProductPageView,
    SuccessPageView,
    CancelPageView,
)
from settings import base

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cancel/', CancelPageView.as_view(), name='cancel'),
    path('success/', SuccessPageView.as_view(), name='success'),
    path('', ProductPageView.as_view(), name='landing-page'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session')
] + static(
    base.MEDIA_URL,
    document_root=base.MEDIA_ROOT
)
