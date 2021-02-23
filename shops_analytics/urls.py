from rest_framework import routers
from django.urls import re_path
from .api import ShopAnalytics

urlpatterns = [
    re_path(r'analytics/$', ShopAnalytics.as_view(), name='analytics'),
]
