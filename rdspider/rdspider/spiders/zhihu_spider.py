#coding:utf-8
'''
1.不登录状态下打开知乎首页，F12后进入Network,勾选上Preseve log,Filter 选择Doc，此时可看到get请求里的Request Headers带有cookies，
里面有_xsrf的值
2.Filter 选择XHR,登陆知乎，注意右边Network里的变化,有一个email,打开，即可看到是post,并且登陆的网站也有，最下面是post需提供的表单信息
'''
import requests

url = 'http://www.zhihu.com'
login_url = 'http://www.zhihu.com/login/phone_num'

header = {'Host': 'www.zhihu.com',
          'Connection': 'keep-alive',
          # 'Content-Length':'100', 这个不注释就会报错，还不知道原因。原因：长度需手动计算
           'Accept':'*/*',
           'User-Agent':' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
           'Referer': 'https://www.zhihu.com/',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.8',
           # ' Accept':'*/*',这个不注释就会报错，还不知道原因
           'Origin':'https://www.zhihu.com',
           'X-Requested-With':'XMLHttpRequest'
          }

s = requests.session() #session 会话对象可跨请求保持某些参数，也会在同一个Session实例发出的所有请求之间保持cookies
r= s.get(url,headers = header)  #这里必须是url里的xsrf
print(r.cookies)
#<RequestsCookieJar[<Cookie cap_id="...a" for .zhihu.com/>, <Cookie n_c=1 for .zhihu.com/>, <Cookie q_c1=...0 for .zhihu.com/>,
# <Cookie _xsrf=2df75e9fee83f23cc3acf67ebd9d4ba5 for www.zhihu.com/>]>

xsrf=r.cookies['_xsrf']#这里简化了_xsrf的获取,在像url的get请求中，Request Headers里的cookies就含有了_xsrf
print(xsrf)#2df75e9fee83f23cc3acf67ebd9d4ba5

email = input('Please input your email: ')
password = input('Please input your password: ')#怎么在输入时直接变为####，不明文显示

data={
    'phone_num':email,
    'password':password,
    '_xsrf':xsrf,
    'remember_me':'true'
}

login = s.post(login_url,headers = header, data = data)  
#登陆的时候用到的xsrf必须为url里的xsrf,而不是login_url里的xsrf,否则就被403
#因为login_url无法在浏览器打开，只会被重定向到url
print(login)  #<Response [200]>  成功
my_cookie = login.cookies
print(my_cookie)
#<RequestsCookieJar[<Cookie n_c=...1 for .zhihu.com/>,
# <Cookie unlock_ticket="...1" for .zhihu.com/>,
#  <Cookie z_c0="..." for .zhihu.com/>]>

test = 'https://www.zhihu.com/people/huarui.pku'
t = s.get(test,headers = header,cookies = my_cookie)#测试，用post登陆得到的cookies，是可以打开知乎用户的界面了
print(t) #<Response [200]>
print(t.content)  #https://www.zhihu.com/people/qing-nan-51-71  运行后打开，网页还是未登录状态，怎么能直接打开已登录的那个网页呢？
