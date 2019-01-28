"""sichuan_yd_video URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.index),
    url(r"^index2$", views.index2),
    # # 二级页面
    # re_path(r'^kind/(?P<kindKey>[\w]+)/$', views.resource_kind),
    # # 三级页面
    # re_path(r'^collection/(?P<collectionKey>[\w]+)/$', views.resource_collection),
    #
    # # re_path(r'^playVideo/(?P<collectionKey>[\w]+)/$', vPlayvideo.collection_play_video),
    # re_path(r'^playVideo/(?P<collectionKey>[\w]+)/(?P<videoCorrelateID>[\w]+)/$', vPlayvideo.video_collection_play_video),
    # url(r"^freeCollection.do$", views.freeCollection),  # 免费专辑
    # # (r"^js_log.do$", views.js_log),  # 播放视频
    #
    # # 特殊功能
    # #  搜索
    # url(r"^searchFilter.do$", vUtils.searchFilter),
    # url(r"^searchAjax$", vUtils.searchAjax),
    # #  收藏
    # url(r"^myFavirity.do$", vUtils.myFavirity),
    # url(r"^myFavirity/AjaxGet", vUtils.myFavirityAjaxGet),
    # url(r"^myFavirity/AjaxIsPut", vUtils.myFavirityAjaxIsPut),  # 是否收藏，yes or no
    # url(r"^myFavirity/AjaxPut", vUtils.myFavirityAjaxPut),
    # url(r"^myFavirity/AjaxDelete", vUtils.myFavirityAjaxDelete),
    # # 三级页面的查找，即查询专辑内容
    # url(r"^resourcesCollection/AjaxGet$", vUtils.resourcesCollectionAjaxGet),
    # # 历史记录
    # url(r"^recentlyWatch.do$", vUtils.recentlyWatchStaticView),
    # url(r"^recentlyWatch/AjaxGet$", vUtils.recentlyWatchAjaxGet),
    # url(r"^recentlyWatch/AjaxPut$", vUtils.recentlyWatchAjaxPut),
    # url(r"^recentlyWatch/AjaxDelete$", vUtils.recentlyWatchAjaxDelete),
    # #  推荐
    # url(r"^recommend/AjaxGet$", vUtils.recommendAjaxGet),

]
