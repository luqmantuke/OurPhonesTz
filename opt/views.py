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


def handler404(request, exception):
    return render(request, '404.html', status=404)



def handler500(request):
    return render(request, '500.html', status=500)
