from django.shortcuts import render
from .models import Guoke

def index(request):
    context_dict = {}
    guokrs = Guoke.objects.all()
    context_dict['guokrs'] = guokrs
    return render(request, 'tt/index.html', context_dict)
    
