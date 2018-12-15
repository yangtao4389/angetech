# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views,v_token_related,v_menu

urlpatterns = [
    url(r'^verifyToken/$', v_token_related.verifyToken),  #
    url(r'^getToken/$', v_token_related.getToken),  #
    url(r'^createMenu/$', v_menu.createMenu),  #
    url(r'^callback.do/$', v_menu.createMenu),  #

]
