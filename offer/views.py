from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import DetailView

from offer.models import Offer



def home(request):
    qs = Offer.objects.all()
    return render(request, 'offer/home.html', {"content": qs})


class OfferDetailView(DetailView):
    queryset = Offer.objects.all()
    template_name = 'offer/detail.html'
