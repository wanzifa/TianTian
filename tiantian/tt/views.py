from django.shortcuts import render
from .models import Guoke,Douban,Zhihu,Huxiu
from .forms import UserForm,UserProfileForm

def index(request):
    context_dict = {}
    zhihu = Zhihu.objects.all()
    huxiu = Huxiu.objects.all()
    douban = Douban.objects.all()
    guoke = Guoke.objects.all()
    context_dict = {'zhihu':zhihu, 'huxiu':huxiu, douban:'douban','guoke':guoke}
    return render(request, 'tt/index.html', context_dict) 

def zhihu_post(request,post_id):
    context_dict = {}
    post = Zhihu.objects.filter(id=1).first()
    post = post.objects.filter(title=post_name).first()
    if not post:
        return render(request, 'tt/404.html')
    context_dict['post'] = post
    return render(request, 'tt/post.html', context_dict)

def zhihu_post(request,post_id):
    context_dict = {}
    post = Zhihu.objects.filter(id=post_id).first()
    if not post:
        return render(request, 'tt/404.html')
    context_dict['post'] = post
    return render(request, 'tt/post.html', context_dict)

def guoke_post(request,post_id):
    context_dict = {}
    post = Guoke.objects.filter(id=post_id).first()
    if not post:
        return render(request, 'tt/404.html')
    context_dict['post'] = post
    return render(request, 'tt/post.html', context_dict)

def huxiu_post(request,post_id):
    context_dict = {}
    post = Huxiu.objects.filter(id=post_id).first()
    if not post:
        return render(request, 'tt/404.html')
    context_dict['post'] = post
    return render(request, 'tt/post.html', context_dict)

def douban_post(request,post_id):
    context_dict = {}
    post = Douban.objects.filter(id=post_id).first()
    if not post:
        return render(request, 'tt/404.html')
    context_dict['post'] = post
    return render(request, 'tt/post.html', context_dict)

def register(request):
    context_dict = {}
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']    
            profile.user = user
            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    context_dict = {'user_form':user_form, 'registered':registered,'profile_form':profile_form}
    return render(request, 'tt/register.html',context_dict)

    
