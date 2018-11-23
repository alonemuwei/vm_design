"""design URL Configuration

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
from mainsite.views import showvm,index_o,index,login,showuser,showuser_o,showbuild,showbuild_o,showclone,showvm_o,vmpart,delvm,closevm,openvm

urlpatterns = [
    url(r'^$',login),
    url(r'^index_o/$',index_o),
    url(r'^vmpart/$',vmpart),
    url(r'index/$',index),
    url(r'^user/$',showuser),
    url(r'^user_o/$',showuser_o),
    url(r'^build/$',showbuild),
    url(r'^build_o/$',showbuild_o),
    url(r'^clone/$',showclone),
    url(r'^vm/$',showvm),
    url(r'^vm_o/$',showvm_o),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^del/$',delvm),
    url(r'^close/$',closevm),
    url(r'^open/$',openvm),
]

