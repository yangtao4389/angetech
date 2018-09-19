# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views,v_token_related

urlpatterns = [
    url(r'^verifyToken/$', v_token_related.verifyToken),  # 日常uv，pv查询
]
