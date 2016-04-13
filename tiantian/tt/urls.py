from django.conf.urls import url
from . import views
from registration.backends.simple.views import RegistrationView

class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return '/tiantian/'

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'zhihu/^(?P<post_id>[\w]+)$', views.zhihu_post, name='zhihu_post'),
        url(r'guoke/^(?P<post_id>[\w]+)$', views.guoke_post, name='guoke_post'),
        url(r'huxiu/^(?P<post_id>[\w]+)$', views.huxiu_post, name='huxiu_post'),
        url(r'douban/^(?P<post_id>[\w]+)$', views.douban_post, name='douban_post'),
        url(r'^register/$', MyRegistrationView.as_view(), name='register')
]
