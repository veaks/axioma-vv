from django.urls import path

from offer.views import home, OfferDetailView

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/', OfferDetailView.as_view(), name='detail'),
]