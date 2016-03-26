from django.shortcuts import render
from .models import GuoKe
from spiders.guoke import contents, titles, times, authors, author_urls

def index(request):
    context_dict = {}
    i=0
    for i in range(4):
        if GuoKe.objects.filter(id=i+1):
            guoke = GuoKe.objects.get(id=i+1)
            guoke.title = titles[i]
            guoke.author = authors[i]
            guoke.time = times[i]
            guoke.author_url = author_urls[i]
            guoke.content = contents[i]
        else:
            guoke = GuoKe(title=titles[i], author=authors[i],
                          time=times[i], author_url=author_urls[i],
                          content=contents[i])
            guoke.save()
       #guoke = GuoKe(title=titles[i], author=authors[i], time=times[i],
               # author_url=author_urls[i], content=contents[i])
        guoke.save()
    context_dict['guokes'] = GuoKe.objects.all()
    return render(request, 'index.html', context_dict)

