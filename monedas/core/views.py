from django.shortcuts import render
from .models import Servicio

# Create your views here.
def index(request):
    servicios = Servicio.objects.all()
    context = {}
    context['servicios'] = servicios
    return render(request, 'index.html', context=context)
