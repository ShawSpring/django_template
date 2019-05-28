'''
这是一份 单文件轻量级django项目的自定义模板，以此为模板创建名为foo的新项目命令如下
django-admin startproject foo --template=django_template
django_template指的是本文件夹的名字，会将本目录下的所有东西创建一份

'''



'''
设置
'''
import os
import sys
from django.conf import settings

'''
使用环境变量来配置（下面的代码也要跟着改）
例如使用时 export/set DEBUG=off
'''
DEBUG = os.environ.get("DEBUG","on")=="on"
ALLOWED_HOSTS=os.environ.get("ALLOWED_HOSTS","localhost").split(',')

# SECRET_KEY = os.environ.get("SECRET_KEY",os.urandom(32))
SECRET_KEY = os.environ.get("SECRET_KEY",'{{secret_key}}')
 # 以本文件为项目模板，每次创建新项目会创建一个随机秘钥，这样保证secret_key在项目层面是固定的，项目间是随机的

settings.configure(
    DEBUG=True,
    SECRET_KEY='thisisthescretkey',
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=[],
    MIDDLEWARE_CLASSES=[
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ],
)




'''
views
'''
from django.conf.urls import url
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello World')


'''
url patterns
'''

urlpatterns = [url(r'^$', index, name="index"),]



'''
manage project
'''
from django.core.wsgi import get_wsgi_application

application =  get_wsgi_application() ##创建 wsgi应用, 这样就能被 WSGI规范的web服务器
'''
application 是大多数 WSGI服务器所用的一个 约定成俗的名字
wsgi应用服务器 有许多 包括Apache下的，
 这里使用 pip install gunicorn 然后命令： gunicore hello 运行它（加参数--log-file=- 向控制台输出日志，）
Gunicorn 服务器作为wsgi app的容器，能够与各种Web框架兼容（flask，django等）,
得益于gevent等技术，使用Gunicorn能够在基本不改变wsgi app代码的前提下，大幅度提高wsgi app的性能。　
'''

if __name__ == '__main__':
   
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)


