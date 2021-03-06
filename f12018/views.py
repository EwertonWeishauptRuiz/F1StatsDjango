from django.shortcuts import render
from django.template import loader
from f12018.models import Driver

# Create your views here.


def index(request):
    all_drivers = Driver.objects.all()
    template = loader.get_template('f12018/index.html')
    context = {
        'drivers': all_drivers
        }
    return render(request, 'f12018/index.html', context)


def driver(request, driver_id):
    return HttpResponse('Driver %s' % driver_id)
