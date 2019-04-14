from tropic import views
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from django.conf import settings
"""tropicCollector URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
 
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/',views.home),
    url(r'^$',views.home), #这儿这个就是根目录
    url(r'^backhome/',views.backhome),
    url(r'^test/',views.test),

    url(r'android/',views.android),
    
    url(r'androidAscy/',views.androidAscy),
    
    url(r'^www/',views.www),

    url(r'^usermanagement/',views.userManagement),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    #url(r'^ueditor/',include('DjangoUeditor.urls' )),

    url(r'^city\.png$', RedirectView.as_view(url='/static/media/city.png')),
    url(r'^editpage/' ,views.editpage),
    url(r'^terminal_svr', views.terminal_svr,name='terminal_svr'),
    url(r'^login', views.login,name='login'),
    url(r'^randomtopic', views.randomTopic,name='randomTopic'),
    url(r'^signactivity', views.signactivity,name='signactivity'),
    
    url(r'^detail',views.detail,name='datail'),
    # url(r'^captcha/', include('captcha.urls')),
    
    url(r'^topic',views.topic),
    

    
]  
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 