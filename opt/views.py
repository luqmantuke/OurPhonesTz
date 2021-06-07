from django.shortcuts import render
from .models import NewArrivals, Iphones, Samsung

def home(request):
    new_arrivals = NewArrivals.objects.all()
    iphones = Iphones.objects.all()
    samsung = Samsung.objects.all()
    context = {
        'newarrivals': new_arrivals,
        'iphones': iphones,
        'samsung': samsung,

    }
    return render(request, 'index.html', context)

