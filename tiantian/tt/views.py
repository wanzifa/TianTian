from django.shortcuts import render
from .models import Guoke,Douban,Zhihu

def index(request):
    context_dict = {}
<<<<<<< HEAD
=======
    douban = Douban.objects.all()
>>>>>>> 534ad2a75abaadc4ef88c61708245d352e5488db
    zhihu = Zhihu.objects.all()
    context_dict['zhihu'] = zhihu
    return render(request, 'tt/index.html', context_dict)
    
