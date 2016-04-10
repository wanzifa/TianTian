from django.shortcuts import render
from .models import Guoke,Douban,Zhihu

def index(request):
    context_dict = {}
    zhihu = Zhihu.objects.all()
    context_dict['zhihu'] = zhihu
    return render(request, 'tt/index.html', context_dict)
    
