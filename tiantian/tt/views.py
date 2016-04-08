from django.shortcuts import render
from .models import Guoke,Douban

def index(request):
    context_dict = {}
    douban = Douban.objects.all()
    context_dict['douban'] = douban
    return render(request, 'tt/index.html', context_dict)
    
